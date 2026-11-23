# Templates e exemplos do TechDocs

[English](README.md)

Templates de páginas e sites do [TechDocs](https://backstage.io/docs/features/techdocs/) (MkDocs) e um exemplo
preenchido de cada um, organizados pelo [Diátaxis](https://diataxis.fr/):

| Categoria                                 | O leitor quer              | Templates                                                                                                    |
|-------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------|
| [Tutoriais](templates/pt-br/tutorials)    | Aprender fazendo, do zero  | Tutorial, Onboarding, Golden path                                                                            |
| [Guias](templates/pt-br/how-to-guides)    | Fazer uma tarefa conhecida | Guia, How-to curto, Runbook, Solução de problemas                                                            |
| [Referência](templates/pt-br/reference)   | Consultar                  | Página inicial do serviço, Operação e suporte, Referência de API, Página de wiki, Notas de versão, Glossário |
| [Explicação](templates/pt-br/explanation) | Entender o porquê          | Arquitetura, ADR, Postmortem, RFC / design doc                                                               |

E quatro [templates de site](templates/pt-br/sites): docs de serviço, wiki de time, golden path e um site em
branco.

Os [exemplos](examples/pt-br/docs) descrevem um serviço de pagamentos fictício, em português e em
[inglês](examples/en/docs). Cada um é um site do TechDocs: registre o `catalog-info.yaml` no Backstage para lê-los
renderizados.

## Usar no VS Code

A extensão [TechDocs Editor](https://marketplace.visualstudio.com/items?itemName=edtroleis.techdocs-editor) traz
estes templates: **Nova página** lista por categoria, e **Ver exemplo** abre a página preenchida.

## Fazer o da sua empresa

1. Faça um fork deste repositório (ou crie um com a mesma estrutura).
2. Mude, tire ou acrescente templates em `templates/<idioma>/<categoria>/`. Um template é uma página Markdown
   com front matter (veja o [README em inglês](README.md#make-your-companys-own) para o formato completo).
   `{{title}}`, `{{date}}`, `{{site_name}}` e `{{owner}}` são preenchidos pelo editor; os outros campos são
   perguntados. Um template de site é um diretório em `sites/` com um `template.yml` e os arquivos dele.
3. Aponte a extensão para o seu repositório, em um de três níveis (o mais específico vale):
    - **Cada pessoa:** a engrenagem da visão TechDocs, ou a configuração
      `techdocsEditor.templates.repository: sua-org/seus-templates/templates`.
    - **Um repositório de documentação:** `templates.repository` no `.techdocs-editor.yaml` dele, para todo mundo
      que abre aquele repositório usar os seus templates.
    - **A empresa inteira:** a mesma configuração distribuída pelo TI como política do VS Code.

## Contribuir

Abra um pull request. O CI confere o Markdown, gera os dois sites de exemplo com `mkdocs build --strict`, confere
o front matter dos templates e se inglês e português têm os mesmos arquivos.

## Licença

[Apache-2.0](LICENSE)
