---
name: godot-template
description: >
  Build and edit a Godot project that uses this folder layout: art finished
  outside the engine, clips under animations/, gameplay under source/.
  Use when the user works in this template, asks where a file belongs, or
  changes the scene tree, animation, rendering, UI, actions, camera, models,
  physics, companions, audio, global state, lighting, import, shipping,
  shaders, input, or effects. Use when the user runs /godot-template.
---
How to build a game in this folder layout. Art is finished outside Godot and exported in. Godot holds scenes, gameplay, and the shipping shell. Read `README.md` for the folder map. This file is the runtime rule for each system.

## Scene tree

The shipping game starts at one root scene. That scene instances the interface, the audio players, and one level from `source/levels`. The level instances the player from `source/entities` and the exported set from `assets/sets`. Do not flatten those children into the parent file.

An instanced scene is one node in the parent. Its children stay in its own `.tscn`. Open that scene to edit them. Turn on editable children only when the parent must override a transform or a property. The parent file then stores an `[editable]` path, and the children show in the current tree with a different tint. Nodes you added yourself in this file always expand in place.

At runtime the instances are real nodes. While the game is playing, read the live tree from the remote scene view. The local view still shows the file you authored.

Name the root of a scene after the file. Keep gameplay nodes (player, items, triggers) as siblings of the big set instance, not buried inside the exported art.

## Animation

Finish every clip in Blender before it enters the engine. The `.blend` lives in `blender/animations/` on a rig from `blender/characters/`. Export one shot per folder under `animations/` as glTF. Reimport writes a text `.tres` of bone tracks beside the glTF and registers the name in that character's animation library under `assets/char`.

Three files, three jobs:

| File | Holds |
|---|---|
| Clip `.tres` in `animations/` | Keyframes: which bone, which time, which pose. |
| Library `.tres` next to the character | The name table. A clip name points at the clip file. |
| State machine `.tres` in `source/entities` | Which state plays which library entries, and how they blend. |

The `AnimationPlayer` on the imported model plays only names that are in its library. The `AnimationTree` on the character points at that player. Its graph is drawn in the editor. The character script does not call `play()` on a clip. It calls `travel("StateName")` or `start("StateName")` and sets blend parameters (`blend_position`, time scale, additive amount) from speed and input.

Use `travel()` when a drawn transition should blend. Use `start()` to cut. A state can contain another blend: locomotion is one state, and inside it a blend space maps walk, jog, and run along one axis. An additive node layers a one-shot, such as a shout, on top of the body without leaving the state.

Clips that are a fixed camera shot (intro, ending, attaching an item) play as one animation. They do not need a blend space. Cycles, one-shots, poses, and paired actions can share `animations/` and are split by folder or by name. Each character has its own library.

## Rendering pipeline

Use the Forward+ renderer unless a platform forces a simpler backend. Set that in the project settings, not in a scene.

Per mesh, a `ShaderMaterial` in `source/shaders` supplies surface data (`ALBEDO`, normals, roughness, alpha). It does not light the pixel. Lights, shadows, and the environment are the pipeline's job. See Shaders for how to write the material, and Lighting and environment for the world.

Transparent cards use alpha scissor or a hashed depth prepass so they still sort. Draw both sides of a flat card with `cull_disabled`. Keep the expensive material path behind a uniform that defaults off.

Particles and decals are extra draw passes. They should not switch the project renderer.

## UI

Playable interface scenes live in `source/user_interface`: menus, pause, settings, cursor, logos, and fades. They are `Control` nodes, instanced by the root scene, not painted into the 3D level.

Prototypes, wireframes, and design-tool exports stay in `design/ux`. That folder is ignored by the importer. When a picture becomes a real control, move the shipped art next to the scene or into `assets/textures`, and leave the prototype where it is.

Drive screens from the global game state. A menu state shows the menu and sets `bypass_controls`. A play state hides the menu and captures the pointer. Use a fade scene for the cut. Do not toggle dozens of controls from gameplay scripts. One UI root listens to the state autoload.

Theme and font belong to the UI scenes. The cursor changes when the input mode changes between pointer and pad.

## Action control

The state machine in Animation is the action graph. Input only supplies a vector and a one-frame action press. The character script, in `_physics_process`, turns that into a state name.

Typical gates:

- Vector long enough, and the body is actually moving: locomotion.
- Pulling a companion and speed collapses: a pull state.
- Blocked by geometry while still pushing the stick: a push state.
- Action pressed, and the current state allows it: a one-shot (interact, emote, attack).
- Scripted beat: the sequence calls `start()` so the cut ignores the stick.

Transitions that should happen on their own use auto advance. Transitions that wait for the script use enabled advance, which fires only on `travel()`. If a blend parameter seems to do nothing, the machine is still in another state.

Cancel a one-shot only when the stick passes a threshold you chose. Do not cancel on any tiny deflection.

## Camera

Put the camera rig in the player scene under `source/entities`, as a sibling of the avatar, not inside the exported mesh. A spring arm or a script keeps a distance and a pitch. Follow the avatar's ground position, not every bounce of the skeleton.

Mouse mode and controller mode can share one rig. Change sensitivity or whether the pointer is captured when the input mode signal fires. Do not invent a second camera for the pad.

Constrain the rig with zones in the level (a marker the camera is pulled toward) instead of hard-coding room names in the camera script. Shake is a short offset on the rig, triggered by the effect script, and it decays to zero. A story sequence may parent the camera or play a fixed shot. When the sequence ends, return the rig to the player.

## Model assets

A prop is a single object a character can use. A library piece is a repeated part of the set. A set is many library pieces nested in the art tool and exported as one scene. Characters are their own export, with a skeleton and an `AnimationPlayer`.

Files:

| Kind | Folder |
|---|---|
| Character glTF and the thin scene that wraps it | `assets/char` |
| Repeated parts | `assets/lib` |
| Interactive objects | `assets/props` |
| Assembled chunks | `assets/sets` |
| Shared textures | `assets/textures` |

The wrapper scene holds the imported glTF instance, the animation player, and the library. Gameplay (movement, interaction, state machine) is a scene in `source/entities` or `source/levels` that instances the wrapper. Do not put gameplay scripts on the exported model except a tiny behavior that truly belongs to that art file.

Collision shapes can be authored as simple meshes in the art tool and created on import. The obstacle script in `source/obstacles` only sets layers and groups. It does not replace the mesh.

## Physics and terrain

Use collision layers, not node names, to tell the ground apart. One layer for solid walls, one for trips, one group or layer for slow ground, one for slick ground. The detector on the character (a ray or the floor the body reports) writes the current surface each physics frame.

The character script reads that surface when it picks speed. Slow ground lowers the cap. Slick ground keeps velocity instead of braking. A trip object in `source/obstacles` signals the body, and the action control changes to a stumble state. Do not slow the character inside the mesh's material, and do not put the speed formula on the prop.

## Companion constraint

The second character is a sibling in the player scene. It does not read the move actions. A constraint in that same scene, usually a line or a physics joint from avatar to companion, limits the distance.

The avatar script sends the shared movement vector into its own speed. The companion script follows the constraint, plays its own state machine, and reads the vector's length only to decide if it is being dragged too hard. Paired animations (a comfort beat, a pull) are two clips, one in each library, started together by the sequence or by the avatar when both state machines are in a matching state.

## Audio

Keep the files in `assets/music` and `assets/sfx`. Keep the players in `source/audio`: one music player, one gameplay sound player, one UI sound player. Gameplay calls the player by bus. It does not instance streams all over the tree.

Music changes by area. A trigger in the level, or a zone script, tells the music player which stream to fade to. Do not switch tracks from a character animation. UI sounds follow the UI state. Duck music under a story sequence if the sequence asks.

Set the bus layout once on the project. Footsteps can follow the terrain detector: a different sample per surface, still through the sound player.

## Global state

Autoloads in `source/globals` are the shared memory. Register them in the project settings.

| Autoload | Holds |
|---|---|
| Game state | Which screen is up, and the quest flags. |
| Context | Live references: avatar, companion, camera, current level. The level and the player register themselves when they enter the tree. |
| Input | The device mode and the movement vector. See Input. |
| Save and settings | What persists, and the options the menu writes. |

Systems find each other through these names. Do not export node paths across scenes for things that always exist. A sequence reads quest flags from the game-state autoload and writes them when a beat finishes.

Pause with the tree pause flag. Leave the UI process mode on so the menu still runs. Reset input when the state leaves play.

## Lighting and environment

One `WorldEnvironment` scene in `source/lighting` is instanced by the level: sky, ambient light, fog, and tonemap. Extra lights live in the set or in the level, not inside character models.

Change the environment from a sequence or a zone when the place really changes. Do not animate the sky from a material shader. Local lights are cheaper to art-direct than one global illumination mode that the target hardware cannot hold. If you drop a heavy global mode, add a few lights where the read of the space needs them.

## Import conventions

The glTF import plugin in `addons/blender_studio_gltf_import` runs when a glTF is reimported. Mark the Blender scene extras before export:

- `asset_type` is `ANIMATION` for a clip, or the character or prop type for a model.
- `anim_type` is `LOOP` when the clip cycles.
- `ref_asset_id` points at the character that owns the skeleton.

The plugin writes the clip `.tres` beside the glTF at 24 frames a second, with the animation optimizer off so keys are not stripped. It loads `asset_index.json` at the project root, finds the character path, and `add_animation`s the clip into that character's library `.tres`. Materials with an id in `material_index.json` are stored as external resources.

Register a character in `asset_index.json` before the first clip import. The state machine is not in the glTF. Draw it in the engine after the library has the names.

Godot AI (`addons/godot_ai`) is the other default plugin. It is an editor bridge for an MCP client. It is not part of the exported game. Install it from its published release into `addons/godot_ai`.

## Shipping

`project.godot` names the main scene and the autoloads. The main scene is the shell in the project root or under `source/`: logos, menu, fade, and the level. Test levels stay in `source/levels` and are not the main scene.

Export presets live in `export_presets.cfg`. Store page art and the trailer live in `marketing/steam` and are uploaded to the store. They are ignored by the importer and are not in the game package. In-game video, such as a credits film, is `assets/videos` and is played by a sequence.

A feature-complete build can still need a bug and performance pass before the public export. Keep that pass on the same main scene. Do not point the export at a test level.

## Shaders

Write `.gdshader` files in `source/shaders`. Start from the engine standard material. Do not write a lighting model.

1. `shader_type` is `spatial` for a mesh, `canvas_item` for UI, `particles` for particle motion.
2. `render_mode` keeps the engine diffuse and specular models. Change culling or blend only when the art needs it.
3. `uniform` values are the inspector knobs. Share them through one `.gdshaderinc` included by each variant.
4. `vertex()` edits position and UV. `fragment()` assigns `ALBEDO`, `NORMAL_MAP`, `METALLIC`, `ROUGHNESS`, and `ALPHA`.

A `ShaderMaterial` points at the shader and sits on the mesh. Split files by use (world, interface, particle card, decal). A new look is a `uniform bool` that defaults off. The expensive path, such as many texture samples to fake thickness, runs only when that switch is on. Stepped motion snaps `TIME` to a fixed step. Park experiments behind `if (false)` in the same file until they earn a switch.

## Input

One autoload in `source/globals` reads devices and publishes `movement_vector`. Register the actions in the project input map. Gameplay scripts do not hard-code scancodes.

| Action | Binding | Use |
|---|---|---|
| `Move Left`, `Move Right`, `Move Up`, `Move Down` | Left stick, with a deadzone | Controller movement |
| `Action` | One face button and one mouse button | A one-shot act |
| `Quit` and debug toggles | Keyboard | Debug builds only |

A mouse, touch, or key event selects mouse mode. A joypad event selects controller mode. Emit a signal on the change. Build the vector only during play and intro. `bypass_controls` clears it for menus and locks. Reset it when leaving play.

Controller mode copies `Input.get_vector()` on the four move actions. Mouse and touch mode adds captured relative motion into a virtual stick, clamps it to an outer radius, and remaps the band between an inner radius and that outer radius from 0 to 1. The vector remains when the pointer stops, so the body keeps moving until the player returns it to the center.

The character turns the vector into `(x, 0, y)`. Length scales speed up to the ground's cap. A short vector is a stop. `Action` is one frame and does not steer.

## Effects

An effect scene in `source/fx` is something the character enables for a few frames. Particles are one piece of it.

Use `GPUParticles3D` for many particles and `CPUParticles3D` when a script must touch each particle. Set `amount`, `lifetime`, and `explosiveness`. A value of `1` bursts. A value of `0` streams. The process material (or a `shader_type particles` shader) moves each particle. The draw pass is the mesh and the material that draws it. The character script sets `emitting` and `amount_ratio` only.

A trail left on the ground is a `MultiMeshInstance3D` or a line, not a particle.

### A complete ultimate

Time the move from one one-shot clip in `animations/`. The character script travels to that state, then enables the rest on frames inside the clip.

1. **Animation.** The clip is the clock. Do not enable the hitbox on frame zero if the swing has not arrived.
2. **Particles.** On the release frame, set `explosiveness` to `1` and `emitting` to true. Stop when the burst ends. A blade arc can be a mesh on the weapon bone instead.
3. **Shader.** Animate a `uniform` on the character shader for a flash or a dissolve, then set it back.
4. **Light, camera, sound.** Switch them on in the same frame as the burst. They live on the effect scene. Camera shake is the offset described in Camera.
5. **Hitbox.** Enable the attack shape only on the active frames. The effect still playing does not mean the hit is still active.

Instance the effect under the character in `source/entities`. When the animation finishes, hide the effect, clear the uniform, and disable the hitbox.
