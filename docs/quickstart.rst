Quickstart
----------

`ourtils` can help with things like combining similar columns:

.. ipython:: python

   import pandas as pd
   from ourtils.wrangling import squish
   mydf = pd.DataFrame({
      'index_col': ['a', 'a', 'b', 'b'], 
      'col_a_1': [1, 2, 30, 40], 
      'col_b_2': [3, 4, 50, 60]
   })
   mydf 
   squish(mydf, index_var='index_col', col_sep='_', agg_func= list)

Or creating new columns in a dataframe:

.. ipython:: python

   import pandas as pd
   from ourtils.wrangling import create_column
   mydf = pd.DataFrame({
      'group': ['a', 'a', 'b', 'b', 'c'], 
      'score': [60, 61, 15, 16, 99]
   })
   mydf

   def create_score_message(group_name: str, total_score: int) -> str:
      return f"Group {group_name} had a score of {total_score}"

   (
      mydf
      .pipe(create_column, 'newcolumn', create_score_message, 'group', 'score')
   )
    

Or compare dataframes with the same columns before / after an operation:

.. ipython:: python

   import pandas as pd
   from ourtils.diffs import DataFrameDiffer
   database_before = pd.DataFrame({'a': [1, 2, 3]})
   database_after = pd.DataFrame({'a': [1, 2]})
   diffy = DataFrameDiffer(database_before, database_after, "a")
   print(diffy.create_report())
   diffy.combined