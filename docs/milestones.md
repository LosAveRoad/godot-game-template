# Milestones and the tree

Where each milestone shows up once the project is laid out in these folders. Dates match the production log.

## Prototype — January 2025

Paper reference, layout models, and a test floor. A character can move. The forest art is not in yet.

- `assets/char` — layout models only.
- `assets/textures` — scans and grid textures used to judge scale.
- `source/levels` — the test level, not the shipping map.
- `source/entities` — the first controllable character.

## Pipeline and obstacle course — February 2025

Export from Blender works. Movement is tested with stand-in obstacles before the paper models are done.

- `addons/` — the import plugin.
- `tools/` — import helpers that are not the editor plugin.
- `assets/lib` and `assets/props` — first exported pieces. Props are the interactive ones.
- `source/obstacles` — collision and reaction scripts. Meshes stay in `assets/`.
- `source/levels` — obstacle-course build beside the future level.
- `tests/` — checks for shared helpers such as value slicing.
- `animations/` — first cycles, registered onto characters by the importer.

## Vertical slice — 3 March 2025

One area looks and plays like the game. Pre-production ends.

- `assets/sets` — the dressed slice.
- `assets/char` — final rigs, not layout models.
- `animations/` — cycles that blend.
- `source/entities` — both characters, the leash, and the animation state machines.
- `source/shaders` — the paper material.
- `source/user_interface` — menu design started, not the final shell.

## Forest, music, intro — March 2025

The slice becomes the map. The quest, the soundtrack, and the opening are in a build.

- `assets/sets` — hub, clearing, pond, fence, and the full world set.
- `assets/props` — branch, tennis ball, shovel, traffic cone, snowman, gate.
- `animations/` — area shots (intro, outro, attach, gate, pond) next to the everyday cycles.
- `source/levels` — the shipping level that instances the world set and the player.
- `source/globals` — quest state, item ids, and pointers to the characters.
- `source/sequences` — gate, and the intro and ending that the 31 March build already contains.
- `source/audio` and `assets/music` — the music manager and area tracks.
- `source/user_interface` — main menu in that same build.

## Effects, creatures, polish — April 2025

The loop stays. The week-to-week work is feel and late life.

- `source/lighting` — the lighting pass.
- `source/fx` — snow, then footsteps and ice.
- `source/obstacles` — shrub topple and bush wiggle.
- `source/user_interface` — cursor behavior.
- `assets/char` — birds and fish.
- `animations/` — paired actions (snuggle, pet, treat) and bird clips.
- `source/sequences` — intro prompts polished against the menu.

## Release shell — May to July 2025

Feature complete in May. Public in July. This pass wraps what March and April already built.

- `source/user_interface` — logos, pause, settings, transitions around the existing menu.
- `source/sequences` — credits on top of the existing intro and ending.
- `source/globals` — save and settings.
- `assets/videos` — the film played with the credits.
- Project root — export presets and the main scene that instances the level and the interface.

Test levels from January and February stay in `source/levels`. They are not the scene the shipped game runs.
