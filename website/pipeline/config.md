# config.yaml

Nineteen thresholds decide every verdict, and all but one were set by
inspection. None are written into code.

Each has a comment where it is defined, giving its justification or stating
plainly that there is none. That includes the detection threshold itself, which
reflects a judgement about how much surveillance loss is tolerable, not a
property of PCR.

Settings that affect scoring are hashed into the screening cache. Changing one
forces a complete re-screen, so a report never mixes old and new rules.

[Known limitations](../limitations.md) sums up how much weight the output can carry.
