# TechDocs templates and examples

[Português](README.pt-BR.md)

Templates for [TechDocs](https://backstage.io/docs/features/techdocs/) (MkDocs) pages and sites, and an example
of each one filled in, organized by [Diátaxis](https://diataxis.fr/):

| Category                                    | The reader wants to       | Templates                                                                               |
|---------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
| [Tutorials](templates/en/tutorials)         | Learn by doing, from zero | Tutorial, Onboarding, Golden path                                                       |
| [How-to guides](templates/en/how-to-guides) | Get a known task done     | Guide, Short how-to, Runbook, Troubleshooting                                           |
| [Reference](templates/en/reference)         | Look something up         | Service home, Operations and support, API reference, Wiki page, Release notes, Glossary |
| [Explanation](templates/en/explanation)     | Understand why            | Architecture, ADR, Postmortem, RFC / design doc                                         |

And four [site templates](templates/en/sites): service docs, team wiki, golden path and a blank site.

The [examples](examples/en/docs) describe a fictional payments service, in English and in
[Portuguese](examples/pt-br/docs). Each one is a TechDocs site: register `catalog-info.yaml` in Backstage to read
them rendered.

## Use them in VS Code

The [TechDocs Editor](https://marketplace.visualstudio.com/items?itemName=edtroleis.techdocs-editor) extension
ships these templates: **New page** lists them by category, and **See example** opens the filled-in page.

## Make your company's own

1. Fork this repository (or create one with the same layout).
2. Change, remove or add templates under `templates/<language>/<category>/`. A template is a Markdown page with
   front matter:

    ```markdown
    ---
    template:
      version: 1
      name: Runbook
      description: Respond to an alert or run an operations procedure
      category: guide            # tutorial | guide | reference | explanation
      example: how-to-guides/runbook.md
      folder: runbooks           # suggested folder, relative to docs/ (optional)
      fields:
        alert:
          prompt: Alert or trigger name
          default: ""
    ---

    # {{title}}
    ```

    `{{title}}`, `{{date}}`, `{{site_name}}` and `{{owner}}` are filled in by the editor; other fields are asked.
    A site template is a folder under `sites/` with a `template.yml` and its files.

3. Point the extension to your repository, at one of three levels (the most specific wins):
    - **Each person:** the gear in the TechDocs view, or the setting
      `techdocsEditor.templates.repository: your-org/your-templates/templates`.
    - **A documentation repository:** `templates.repository` in its `.techdocs-editor.yaml`, so everyone who opens
      that repository uses your templates.
    - **The whole company:** the same setting distributed by IT as a VS Code policy.

## Contributing

Open a pull request. The CI checks the Markdown, builds both example sites with `mkdocs build --strict`, checks
the template front matter and that English and Portuguese have the same files.

## License

[Apache-2.0](LICENSE)
