### Recommendation Engine Guidelines

## Objective

Design a simple relevance-based engine that recommends jobs to a user.

Given a `user_id`, return all jobs ranked from most relevant to least relevant.


## Endpoint

GET /users/{user_id}/recommendations

## Relevance Signals

Your ranking logic should consider the following:

1. Industry Match

   * Exact match between user and job industry should strongly impact relevance

2. Keyword Overlap

   * Count overlapping keywords between user and job
   * Higher overlap → higher relevance

3. Description Similarity

   * Basic text matching is sufficient

## Output Requirements

* Return all jobs
* Sorted by descending relevance score
* Include `job_id` and `score` for each job

## Evaluation Focus

* Logical ranking
* API correctness

No single correct formula exists, but rankings must be reasonable and consistent.
