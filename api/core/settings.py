
JOURNEY_TYPE_CHOICES = (
    (1, 'Health'),
    (2, 'Finance'),
    (3, 'Skill development')
)

JOURNEY_STATUS_CHOICES = (
    (1, 'Preliminary'),
    (2, 'Scheduled'),
    (3, 'Active'),
    (4, 'Finished'),
    (5, 'Overdue'),
    (6, 'Quit'),
)

# Different available types depending on journey type
TASK_TYPE_CHOICES = {
    1: (
        (1, 'Food'),
        (2, 'Excercise'),
        (3, 'Sleep'),
        (4, 'Meditation')
    ),
    2: (
        (1, 'Spending'),
        (2, 'Saving'),
        (3, 'Investing')
    ),
    3: (
        (1, 'Reading'),
        (2, 'Learning'),
        (3, 'Developing')
    )
}

TASK_STATUS_CHOICES = (
    (1, 'Preliminary'),
    (2, 'Scheduled'),
    (3, 'Active'),
    (4, 'Finished'),
    (5, 'Overdue'),
    (6, 'Quit'),
    (7, 'Hold')
)
