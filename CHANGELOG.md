# Changelog

## [0.2.2](https://github.com/jpshackelford/oh-markdown-tool/compare/v0.2.1...v0.2.2) (2026-07-06)


### Bug Fixes

* don't try to create GitHub release (Release Please already does) ([9ed4a0d](https://github.com/jpshackelford/oh-markdown-tool/commit/9ed4a0d8ba5d93d56c8c3a78221a500415208f59))
* make release-please trigger release workflow explicitly ([3502c8b](https://github.com/jpshackelford/oh-markdown-tool/commit/3502c8b9cf6bd746b16f7e3122aa30ca765c5380))

## [0.2.1](https://github.com/jpshackelford/oh-markdown-tool/compare/v0.2.0...v0.2.1) (2026-07-06)


### Bug Fixes

* make CI workflow not run at all on Release Please PRs ([ba25dc7](https://github.com/jpshackelford/oh-markdown-tool/commit/ba25dc7c0724deb38a36caa6dfe3415da5fa9361))
* remove build/publish from release-please, delegate to release.yml ([c6a5569](https://github.com/jpshackelford/oh-markdown-tool/commit/c6a5569f02e0e523135176103d5f2d7c576b71b3))
* return non-empty tool observations to prevent SDK IndexError ([4618bdc](https://github.com/jpshackelford/oh-markdown-tool/commit/4618bdc553907de39b8c8b8076b200a4f5978eb3)), closes [#14](https://github.com/jpshackelford/oh-markdown-tool/issues/14)
* use shields.io badges for PyPI instead of badge.fury.io ([b312a33](https://github.com/jpshackelford/oh-markdown-tool/commit/b312a33dcc01d20a2055203fb3ff30aaab4bd8f6))

## [0.2.0](https://github.com/jpshackelford/oh-markdown-tool/compare/v0.1.0...v0.2.0) (2026-07-06)


### ⚠ BREAKING CHANGES

* Package now requires Python >=3.12 (previously unspecified). Tool integration moved to optional [openhands] extra - users must install "oh-markdown-tool[openhands]" to use with OpenHands agents.

### Features

* decouple core library from openhands-sdk integration ([0e07468](https://github.com/jpshackelford/oh-markdown-tool/commit/0e0746856837a6b2a9b04d353ddf0c750f9a3b59))
* decouple core library from openhands-sdk integration ([#6](https://github.com/jpshackelford/oh-markdown-tool/issues/6)) ([0e07468](https://github.com/jpshackelford/oh-markdown-tool/commit/0e0746856837a6b2a9b04d353ddf0c750f9a3b59))


### Bug Fixes

* add missing llm-api-key parameter to PR review workflow ([8635726](https://github.com/jpshackelford/oh-markdown-tool/commit/8635726112e37a1b11d3f198562aebc47f40bae1))
* align PR review bot settings with ohtv repository ([0adc3b1](https://github.com/jpshackelford/oh-markdown-tool/commit/0adc3b14465a1865d7fab424c0ee23b36363c8d1))
* make lint/test jobs run (but skip work) for Release Please PRs ([8375729](https://github.com/jpshackelford/oh-markdown-tool/commit/83757293815d9d10319ddd685ab8cfb7c999cdd2))
* make Release Please workflow publish to PyPI directly ([e000eb7](https://github.com/jpshackelford/oh-markdown-tool/commit/e000eb723e9e87cb037787340690fef79dbc4743))
* use LLM_API_KEY secret for PR review workflow ([4e11c49](https://github.com/jpshackelford/oh-markdown-tool/commit/4e11c4996bf5aef8211d06b104572d67e127b15e))

## 0.1.0 (2026-07-06)


### Features

* Add automated PR review with OpenHands ([60b5dd0](https://github.com/jpshackelford/oh-markdown-tool/commit/60b5dd0ee8c6fd9556a3b7d7c77854ab22f6fc5f))
* add automated release workflow with Release Please ([e55618e](https://github.com/jpshackelford/oh-markdown-tool/commit/e55618e23d5165812c6c39e7554c1d181fd71659))


### Bug Fixes

* exclude Release Please PRs from automated code review ([8187966](https://github.com/jpshackelford/oh-markdown-tool/commit/8187966941b961527e6197aa6f832ad3a96ae9c9))
* Update codecov action parameter from 'file' to 'files' ([8df1c85](https://github.com/jpshackelford/oh-markdown-tool/commit/8df1c85aed11b5e03cc3d19791c5463f4eb1ff1e))
* Use --system flag for uv commands in CI ([#7](https://github.com/jpshackelford/oh-markdown-tool/issues/7)) ([5384527](https://github.com/jpshackelford/oh-markdown-tool/commit/53845273e1485acdf1899424db81821f3b272717))

## 0.1.0 (Initial Release)

### Features

* Initial release of oh-markdown-tool
* Structural editing and formatting for markdown documents
* Table of contents generation
* Heading numbering
* Document parsing and operations
* Integration with OpenHands SDK
