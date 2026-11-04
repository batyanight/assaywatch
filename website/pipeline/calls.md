# The calls table

Every later stage reads this file and nothing else. This is deliberate: the four
analyses below cannot disagree about the data, because there is only one copy.

Of the 3.0 million rows in this run, **1.57 million were evaluable** : both
primers bound in the correct orientation and size range, so the result says
something about the assay. The remaining 1.47 million produced no product.

That division is the method's main weakness. A record where one primer has
diverged is scored as a failure, but a record where *both* have diverged is left
out of the denominator entirely. Each assay page gives its own figures.
