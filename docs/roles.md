# Roles

One small team, four months, everyone on the same project. People keep their craft and also pick up the neighboring job when the schedule needs it. Asset status and review notes live in Kitsu. A playable build goes out on the weekly production log.

## Leads

| Role | Owns |
|---|---|
| Director | Game design, scope, and most of the gameplay programming. Decides what the weekly build must contain. Also reviews animation in the engine. |
| Art director | Look, paper-craft designs, color, type, and the mood of the kid. Storyboards the intro and ending. Reviews assets with paintovers. |
| Producer | Schedule against the four-month box, the weekly log, and the release. |
| Executive producers | Studio priority and the decision to spend the year on short projects. Not day-to-day on the level. |
| Technical director | The Blender-to-Godot pipeline, shading, and the hard runtime pieces (leash, effects, intro hookup). |

## Art

| Role | Owns |
|---|---|
| Environment artist | Sets, paths, ground, water, lighting in the level, and dressing the hub, clearing, pond, and fence. |
| Asset artist | Library pieces and props. Tracks each asset in Kitsu from concept to export. A prop is interactive and often rigged. A library piece is placed and repeated. |
| Rigger and animator | Character rigs that survive glTF, and the shots that cannot be a cycle: outro, petting, gate. Fixes rigs when the engine cannot represent a Blender deform, such as stretchy IK. |
| Animator | Cycles first (walk, run, idle), then one-shots. Moves animation off layout rigs onto final rigs. |
| Project coordinator and animator | Animation list, cycle-to-cycle flow, and keeping the weekly plan honest. |

## Game and support

| Role | Owns |
|---|---|
| Director, as programmer | Player, kid, quest state, and the animation state machines in Godot. |
| Technical director, as programmer | Import plugin, level-assembly export, effects, and performance passes. |
| Composer, sound designer, and programmer | Music, area changes, and supporting gameplay code. Comes on after the slice, not from week one. |
| Additional programming | Help on engine-side problems. Not a full-time seat on this project. |
| Additional typography | Font and interface lettering. A short task, not a full-time seat. |
| Git and infrastructure | Repository and the machines the export has to land on. |
| Voice | A few recorded lines. Not on the weekly floor. |

## Who touches which folder

| Folder | Primary |
|---|---|
| `assets/char`, `assets/lib`, `assets/props`, `assets/sets`, `assets/textures` | Asset artists and the environment artist, under the art director. |
| `assets/music`, `assets/sfx` | Composer and sound designer. |
| `assets/videos` | Producer and director, for the credits film. |
| `animations/` | Animators. The technical director's importer files each clip onto a character. |
| `source/entities`, `source/levels`, `source/sequences`, `source/globals` | Director, with the technical director on pipeline-shaped code. |
| `source/audio` | Composer and the director. |
| `source/user_interface` | Art director for look and type. Director for behavior. |
| `source/fx`, `source/shaders`, `source/lighting` | Technical director, with environment art for the lights in the set. |
| `source/obstacles` | Director. Meshes stay in `assets/`. |
| `addons/` | Technical director. |
| `tests/` | Whoever owns the helper being checked. |
| `tools/` | Technical director, for import utilities. |

## How a week runs

1. The director names what the next build has to show.
2. Artists update asset tasks in Kitsu and export through the pipeline.
3. Animators deliver clips. The importer registers them. State machines in Godot are updated only when a new action needs a new state.
4. Programming lands in `source/` and the weekly build is played.
5. The production log records what each person finished. Subscribers can try that build.

The director and the technical director both write code. The art director does not. Animators do not assemble the shipping level in Godot. The environment artist assembles it in Blender and exports the set.
