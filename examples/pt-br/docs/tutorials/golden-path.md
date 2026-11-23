# Golden path: um serviço de backend novo

O jeito recomendado de criar um serviço de backend na Example Corp: Kotlin, Spring Boot, PostgreSQL e a
pipeline de deploy padrão. O Serviço de Pagamentos foi criado assim.

## Quando usar (e quando não)

- **Use** para um serviço HTTP que é dono dos seus dados e roda no cluster da plataforma.
- **Não use** para jobs em lote (veja o golden path de dados) nem para front-ends.

## O que você ganha

- Um repositório com build, testes, lint e varredura de segurança já configurados
- Deploy em staging a cada merge e em produção com uma aprovação
- Dashboards, alertas e logs funcionando desde o primeiro dia
- Um site do TechDocs e um `catalog-info.yaml`

## Antes de começar

- Um time no catálogo que vai ser dono do serviço
- Um nome para o serviço, em kebab case (`payments-service`)

## Passos

1. No Backstage, abra **Create** e escolha **Serviço de backend (Kotlin)**.
2. Preencha o nome, o time dono e uma descrição de uma linha. Clique em **Create**.
3. Abra o repositório novo e faça o merge do primeiro pull request que o template abriu.
4. Espere a pipeline: o serviço aparece em staging em uns 10 minutos.
5. Abra o serviço no catálogo e confira a aba **Docs**.

## Dono do golden path

O time de Plataforma, em `#platform-help`.

## Alternativas

- Jobs de dados: o golden path de dados
- Front-ends: o golden path web
