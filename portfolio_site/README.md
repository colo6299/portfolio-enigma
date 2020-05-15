1. The structure is far more nested than flask, with many separate nested systems of code.

2. The two urls files are specifying different apps' scope over their urls. They interact in a nested fashion, with higher-order url files operating as prefixes to child urls.

3. Splitting code over multiple apps allows for more clear, context-agnostic code which makes relationships between objects easier to understand. Additionally, changes to the code are easier to impliment, with fewer structure-specific references built in.