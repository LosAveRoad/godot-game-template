# Product requirements

## Summary

A short winter walk. The player is a large dog, tied to a small kid, in a paper-craft forest. Together they find a few objects and dress a snowman. One sitting, no fail state, no score attack.

The production is also a pipeline test: characters, props, sets, and animation clips are made in Blender and exported into Godot. Godot holds gameplay, the animation state machines, and the shipping shell.

## Timebox

Four months of production with the whole art team on this project, from January 2025 through a feature-complete build in May 2025. Public release follows after a bug-and-performance pass. The scope stays small enough to finish inside that window. A full game of this density would take years; this one is a micro-game.

## Player fantasy

Be a dog. Lead, drag, or wait for the kid. Explore a small open patch of woods: camp, paths, a pond, a fence. Help the kid, or be a nuisance. The kid's mood shows on their face and in emotes. Nothing ends the run except finishing the snowman and watching the ending.

## Core loop

1. Wake up and meet the kid.
2. Move through snow, ice, and obstacles. The leash keeps the two characters together.
3. Find a decoration and bring it back.
4. Watch the kid attach it to the snowman.
5. Repeat until the snowman is dressed, then play the ending.

Required decorations: a branch, a tennis ball, a shovel, and a traffic cone. Extra places (the gate, the willow, birds, fish) are optional beats, not extra win conditions.

Target length is one short sitting, on the order of 10 to 30 minutes. Knowing the map is the short end. Wandering is the long end.

## Pillars

- Paper, not plastic. Models start as real paper crafts, get scanned, then rebuilt in Blender. Motion is posed like stop-motion, around 24 frames a second.
- Two characters, one leash. The dog is the avatar. The kid is a partner with their own speed, stamina, and mood.
- Made in Blender, played in Godot. Levels are assembled in Blender from library pieces and exported. Godot does not rebuild the sets by hand.
- No fail. Ice, snow, and tripping change how the walk feels. They do not restart the game.

## Content

- One winter map with a camp, paths, a clearing, a pond, and a fenced gate.
- Dog and kid, with locomotion, pulling, pushing, tripping, and a small set of paired actions (pet, lick, snuggle, treat).
- Birds that leave when the dog comes close. Fish in the water. These are late additions, not part of the win condition.
- Intro and ending shots, a main menu, pause, settings, and credits.
- Music that changes by area. Footsteps, snow, and ice as surface effects.

## Pipeline requirements

- A prop is something a character interacts with and that can be animated. A library piece is a repeated environment object. A set is a chunk of the level built by nesting library pieces.
- Export is glTF. Animation clips are separate exports. An import step files each clip onto the right character and writes the Godot animation resource.
- Collision can be marked in Blender with simple shapes and created on import.
- The animation state machine stays in Godot. Blender delivers the clips. The game blends them from speed and input.

## Out of scope

- A long campaign, combat, or an inventory puzzle beyond carrying one find back to the snowman.
- Hand-building the final level inside Godot.
- Baking every possible walk, turn, and bark into one Blender shot. Those mixes are runtime.
- A native engine feature for every pipeline gap. The import plugin covers the project's own export rules. It is not a general product.

## Milestones

| When | Milestone | Done when |
|---|---|---|
| Late January 2025 | Prototype | A dog can be moved, the level plan exists, and paper reference is in progress. |
| Mid-February 2025 | Pipeline and obstacle course | Assets export from Blender into Godot. Core movement through snow, ice, and solid props can be tested. |
| 3 March 2025 | Vertical slice | One area looks and plays like the final game: both characters, the leash, blended locomotion, paper shading. Pre-production ends here. |
| March 2025 | Forest and quest | The full map, the four decorations, the snowman, music, and the intro and menu build are in a playable build. |
| April 2025 | Surface and life | Lighting, snow and ice effects, the cursor, the gate, fish, birds, and paired character actions. |
| 20 May 2025 | Feature complete | The four-month plan is done. Bugs and performance remain. Subscribers can play. |
| 11 July 2025 | Public release | Store pages are up. Remaining fixes from early access are in. |

## Success

The team finishes a complete short game inside four months, using only the Blender-to-Godot path above. A new player can finish the snowman in one sitting without a fail screen. The same tree of folders can be reused for the next project: art in `assets/`, clips in `animations/`, play in `source/`.
