# screen

The computationally dominant stage, and the only one operating on sequence at
scale.

Every oligonucleotide of every assay is searched against every record of its
archive, on both strands, allowing up to six mismatches. Where forward and
reverse sites face each other at a plausible product size, mismatches are
converted to a penalty and the penalty to a call. See
[scoring methods](../scoring.md).

On the run underlying this site, that comprised **3.0 million assay–record
pairs**. Execution is parallelized across cores and the output is independent
of core count, so a faster run is not a different run.

**Results are cached per archive** and reused until an input that could change
them changes. The scoring configuration and the stage's module import closure
are both hashed into the cache key, so modifying a penalty invalidates every
cached screen automatically rather than depending on manual invalidation.

**Output:** one row per (assay, record) giving the call, the penalty, the
product coordinates, and each oligonucleotide's mismatch positions measured
from its 3′ terminus.
