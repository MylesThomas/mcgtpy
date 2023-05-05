# Import methods from our Modules
from mcgtpy.my_stats import print_stats
from mcgtpy.helper_functions import columns_janitor

# Print stats
print_stats()

# Clean columns
old_list = [
    "  MYleS  __    _",
    "  _ chRistian______ George___",
    "____ tHomas ",
]

new_list = columns_janitor(old_col_names=old_list)

print(f"old_list: {old_list} \n")
print(f"new_list: {new_list} \n")