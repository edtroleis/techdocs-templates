# Golden path: a new backend service

The recommended way to create a backend service at Example Corp: Kotlin, Spring Boot, PostgreSQL and the
standard deploy pipeline. The Payments Service was created this way.

## When to use it (and when not)

- **Use it** for an HTTP service that owns its data and runs on the platform cluster.
- **Do not use it** for batch jobs (see the data golden path) or for front-ends.

## What you get

- A repository with build, tests, linting and security scans already set up
- Deploy to staging on every merge and to production with one approval
- Dashboards, alerts and logs that work from day one
- A TechDocs site and a `catalog-info.yaml`

## Before you start

- A team in the catalog that will own the service
- A name for the service, in kebab case (`payments-service`)

## Steps

1. In Backstage, open **Create** and choose **Backend service (Kotlin)**.
2. Fill in the name, the owner team and a one-line description. Click **Create**.
3. Open the new repository and merge the first pull request the template opened.
4. Wait for the pipeline: the service shows up in staging in about 10 minutes.
5. Open the service in the catalog and check the **Docs** tab.

## Owner of the golden path

The Platform team, in `#platform-help`.

## Alternatives

- Data jobs: the data golden path
- Front-ends: the web golden path
