# Contribution Guidelines

Contributions are welcome via GitHub pull requests. This document outlines the
process to help get your contribution accepted.

Please note that this project is released with a
[Contributor Code of Conduct](./CODE_OF_CONDUCT.md). By participating in this
project you agree to abide by its terms.

## How to Contribute

Ensure your pull request adheres to the following guidelines:

1. Fork this repository.
2. Add your awesome cooklang recipes link to [data.yaml](../data.yaml).

```yaml
...
  - description: "Description of your cookbook."
    website:
      name: "Name of your website"
      url: "Url of your website"
    cooklang:
      name: "Name of your your cookbook site with all of your *.cook files."
      url: "Url of your cookbook"
    user:
      name: "Your user name"
      url: "Link to your website or profile."
...
```

3. Install dependencies

```shell
pip install -r ./scripts/requirements.txt
```

4. Render a new `README.md`.

```shell
python scripts/render_readme.py > README.md
```

5. Lint the repo using [awesome-lint][4] and [yamllint][5]

```shell
npx awesome-lint
yamllint .
```

6. Submit a [pull request][3].

Thank you for your suggestions!

## Testing Changes

The README.md may be tested using []`awesome-lint`][1]

## Updating your PR

A lot of times, making a PR adhere to the standards above can be difficult.
If the maintainers notice anything that we'd like changed, we'll ask you to
edit your PR before we merge it. There's no need to open a new PR, just edit
the existing one. If you're not sure how to do that, [here is a guide][2]
on the different ways you can update your PR so that we can merge it.

[1]: https://github.com/sindresorhus/awesome-lint
[2]: https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md
[3]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[4]: https://github.com/sindresorhus/awesome-lint
[5]: https://github.com/adrienverge/yamllint
