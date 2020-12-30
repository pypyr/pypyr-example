# composable pipelines
These examples show 3 different ways to compose pipeline functionality:

- groups
    - have a single pipeline with multiple step-groups
    - there are default step groups that run each time
    - there are additional optional step-groups that run depending on input switches from the cli
- pipes
    - encapsulate functionality in different pipelines
    - each pipeline can run individually
    - the parent (or main entry-point, or orchestrator) pipeline, runs some default setup 
      steps on each run.
    - the various child pipelines run optionally depending on input switches from the cli.
- shared
    - common or shared functionality exist in its own pipeline
    - other pipelines can call this helper pipeline to execute the shared/common steps.
    - this way helper/common code exist in one place.
    - the shared pipeline can also run individually.
