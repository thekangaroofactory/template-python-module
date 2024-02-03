# -- file module
from items import get_item

# -- folder module
from tasks import get_task, set_task

# -- package module
from pkg.issues.get_issues import get_issues
from pkg.milestones.get_milestones import get_milestones

# -- item module
item = get_item()
print(item)

# -- task module
task = get_task()
print(task)

task = set_task()
print(task)

# -- pkg package
issue = get_issues()
print(issue)

milestone = get_milestones()
print(milestone)
