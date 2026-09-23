# Godot game template

Empty folder skeleton for a Godot project that keeps exported art separate from gameplay code. It does not include a `project.godot`, scenes, or sample assets. Create the Godot project in this directory when you are ready to start.

Host the repository in a GitHub organization, not only under a personal account. Organization membership is how art, code, and review stay on one team.

The layout follows a Blender-to-Godot split: art is authored outside Godot and exported in, animation clips live in their own tree, and game logic lives under `source/`.

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

Animation clips exported on their own, one clip (or one shot) per folder. A typical clip is a glTF plus the Godot animation resource produced on import. Character scenes and animation libraries point at these files. Do not put the character mesh here, and do not put the animation state machine here.

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

Editor plugins. Each plugin gets its own subfolder with its `plugin.cfg`. Enable plugins from the Godot project settings after you create `project.godot`.

## tests

Automated checks. A test scene or script belongs here, not inside a shipping level. Run a test scene on its own.

## tools

One-off editor or import utilities that are not part of the running game and are not editor plugins.

## Project documents

These files are blank templates. Fill them for the game you are making. Do not paste in another title's history.

| Document | What to write |
|---|---|
| `docs/prd.md` | Summary, timebox, player fantasy, core loop, pillars, content, pipeline, out of scope, milestones, and success. |
| `docs/roles.md` | Leads, art, game and support, which role writes which folder, and how a week runs. |
| `docs/production-log.md` | One section per week: date, title, and what landed in the build. |
| `docs/milestones.md` | Each milestone's name, done-when, and the folders that show it. |

## Review bot

Install the [OpenHands GitHub App](https://github.com/apps/openhands-agent) on the GitHub organization that owns this repository. In the organization (or this repository) add an Actions secret named `LLM_API_KEY`.

The review workflow does not run on every pull request. After the secret exists, request a review in either of these ways:

- Add the `review-this` label to the pull request.
- Request `openhands-agent` as a reviewer.

Create the `review-this` label under Issues → Labels if it is not there yet. The workflow file is `.github/workflows/pr-review-by-openhands.yml`.

## Suggested first steps

1. Open this folder in Godot and let it create `project.godot`, or create the project from the project manager and point it here.
2. Set the main scene once `source/levels` has a level and the user interface has a menu.
3. Register autoloads from `source/globals`.
4. Export art into `assets/` and clips into `animations/`, then instance those scenes from `source/`.
