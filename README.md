# Godot game template

Empty folder skeleton for a Godot project that keeps exported art separate from gameplay code. It does not include a `project.godot`, scenes, or sample assets. Create the Godot project in this directory when you are ready to start.

Host the repository in a GitHub organization, not only under a personal account. Organization membership is how art, code, and review stay on one team.

The layout follows a Blender-to-Godot split: art is authored outside Godot and exported in, animation clips live in their own tree, and game logic lives under `source/`.

How the engine pieces fit together (scene tree, animation, rendering, UI, actions, camera, models, physics, companion, audio, global state, lighting, import, shipping, shaders, input, and effects) is the harness skill `.grok/skills/godot-template/SKILL.md`. Invoke it with `/godot-template`.

Each folder contains a `.gitkeep` file so Git stores the empty directory. Delete that file once the folder has real content.

## assets

Exported art. These files are the models, images, and sounds the game displays. Gameplay scripts do not belong here.

| Folder | Put here |
|---|---|
| `assets/char` | Character models exported from the art tool (meshes, skeletons, and the animation player that ships with the model). |
| `assets/lib` | Reusable environment pieces: trees, rocks, fences, and other parts that get repeated. |
| `assets/props` | Interactive objects: pickups, doors, and other single items a level can instance. |
| `assets/sets` | Assembled level chunks built from library pieces and exported as one scene. |
| `assets/music` | Music tracks. |
| `assets/sfx` | Sound effects. |
| `assets/textures` | Shared textures that are not already packed inside a model export. |
| `assets/videos` | Video files used by menus, credits, or cutscenes. |

## animations

Finish every clip in Blender before it enters Godot. Author the `.blend` file under `blender/animations/`, on a rig that lives in `blender/characters/`. `blender/.gdignore` keeps those files out of the Godot import.

Export the finished shot as glTF into `animations/`, one clip per folder. The Blender Studio glTF Import plugin reads the scene extras (`asset_type` of `ANIMATION`, `anim_type` such as `LOOP`, and `ref_asset_id`) and writes the Godot animation resource next to the glTF. It then registers that clip on the character library named by `asset_index.json`.

Character meshes stay in `assets/char`. Animation state machines stay in `source/entities`. They choose which imported clip plays. They are not authored in Blender.

## blender

Source files for the art tool. The game does not load them.

| Folder | Put here |
|---|---|
| `blender/characters` | Character rigs. Animation clips are made on these rigs. |
| `blender/animations` | The `.blend` file for each shot. Export only after the clip is finished. |

## source

Gameplay. Scripts and the scenes that assemble the game live here. They instance art from `assets/` and clips from `animations/`.

| Folder | Put here |
|---|---|
| `source/entities` | Actors that move or react: the player, companions, and other interactive characters, including their state machines. |
| `source/levels` | Level scenes that place entities, props, and sets. The shipping level and any test levels both go here. |
| `source/sequences` | One-shot story beats: intro, ending, credits, and scripted events. |
| `source/globals` | Autoload scripts for shared state: progress, input, save data, and settings. |
| `source/audio` | Scripts and scenes that play files from `assets/music` and `assets/sfx`. The audio files themselves stay in `assets/`. |
| `source/user_interface` | Menus, cursor, logos, and screen transitions. |
| `source/fx` | Runtime effects such as footprints, weather, and surface trails. |
| `source/obstacles` | Behavior scripts attached to art objects: collision setup, tripping, and similar reactions. The meshes stay in `assets/`. |
| `source/shaders` | Shaders and shader materials shared by the art. |
| `source/utility` | Small shared helpers used by more than one system. |
| `source/lighting` | World environment and lighting scenes reused by levels. |

## addons

Two plugins are part of the default project setup. After Godot creates `project.godot`, enable both under Project Settings, Plugins.

| Plugin | Path | What it does |
|---|---|---|
| Blender Studio glTF Import | `addons/blender_studio_gltf_import` | Already in this repository. On glTF reimport, saves each Blender animation to a `.tres` and adds it to that character's animation library. |
| Godot AI | `addons/godot_ai` | [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai), Godot 4.7 or newer. Install a published release so `plugin.cfg` is at `addons/godot_ai/plugin.cfg`. It connects an MCP client to the open editor. |

In `project.godot` the enabled list is:

```
[editor_plugins]

enabled=PackedStringArray("res://addons/blender_studio_gltf_import/plugin.cfg", "res://addons/godot_ai/plugin.cfg")
```

Godot AI is not copied into this repository. Follow that project's release install. Do not paste a source snapshot over an existing `addons/godot_ai` folder.

The import plugin looks up characters in `asset_index.json` and materials in `material_index.json` at the project root. Add an entry before importing a new character's clips.

## tests

Automated checks. A test scene or script belongs here, not inside a shipping level. Run a test scene on its own.

## tools

One-off editor or import utilities that are not part of the running game and are not editor plugins.

## design

Reference pictures for the team. The game does not load these files. `design/.gdignore` tells Godot to skip the folder, so the pictures are not imported and are not packed into the game.

| Folder | Put here |
|---|---|
| `design/concepts` | Concept art, mood images, character and environment reference, and scans of paper models. |
| `design/ux` | Wireframes, flow diagrams, UI prototypes, and exported boards from a design tool. |

Finished interface art is separate. Menu backgrounds, icons, and the cursor that the game actually shows go in `source/user_interface`. Textures shared by materials go in `assets/textures`.

## marketing

Store listing files. Players never download these inside the game. `marketing/.gdignore` keeps Godot from importing them.

| Folder | Put here |
|---|---|
| `marketing/steam` | Steam store images and video: header capsule, small capsule, main capsule, library capsule, library header, page background, screenshots, and the trailer. Upload these in Steamworks. They do not go in `assets/`. |

## Project documents

These files are blank templates. Fill them for the game you are making. Do not paste in another title's history.

| Document | What to write |
|---|---|
| `docs/prd.md` | Summary, timebox, player fantasy, core loop, pillars, content, pipeline, out of scope, milestones, and success. |
| `docs/roles.md` | Leads, art, game and support, which role writes which folder, and how a week runs. |
| `docs/production-log.md` | One section per week: date, title, and what landed in the build. |
| `docs/milestones.md` | Each milestone's name, done-when, and the folders that show it. |

## Pull requests

Every pull request must use `.github/pull_request_template.md`. The body needs three filled sections: `Summary`, `Org templates`, and `Templates stay blank`. HTML comments alone do not count.

`.github/workflows/pr-template.yml` runs on each pull request open, edit, update, reopen, and ready-for-review event. It calls `tools/check_pr_body.py`. A missing or empty section fails the check.

## Suggested first steps

1. Open this folder in Godot and let it create `project.godot`, or create the project from the project manager and point it here.
2. Set the main scene once `source/levels` has a level and the user interface has a menu.
3. Register autoloads from `source/globals`.
4. Export art into `assets/` and clips into `animations/`, then instance those scenes from `source/`.
