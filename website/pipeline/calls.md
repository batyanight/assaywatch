# The calls table

Every subsequent stage reads this file and nothing else. This is deliberate:
the four analyzes below cannot disagree about the data, because a single copy
exists.

Of the 3.0 million rows in this run, **1.57 million were evaluable** — both
primers bound in the correct orientation and size range, so the result is a
statement about the assay. The remaining 1.47 million produced no product.

That division is the principal weakness of the method: a record in which one
primer has diverged is scored as a failure, whereas a record in which *both*
have diverged is excluded from the denominator entirely. Each assay page
reports its own figures.
