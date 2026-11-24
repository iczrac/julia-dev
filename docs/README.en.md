# Julia Dev Squad (主理呀開發團)

> **Language / 語言**：[繁體中文](../../README.md) · English (this file) · [简体中文](README.zh-Hans.md)

The team name comes from Julia the lead's Chinese pun 「主理呀」 (*zhǔlǐya*) — analyze the task first, then orchestrate the workflow, then deliver. "Julia" is kept as the lead's call sign; "Squad" emphasizes that this is a team, and avoids being misread as development for the Julia programming language.

A full-spectrum software development expert squad orchestrated by Julia. Whether it's source-code reverse engineering, greenfield builds, feature work, bug fixes, refactoring, reviews, migrations, third-party integrations, data/AI applications, or delivery decks, the squad always classifies the task type first, then dispatches the most suitable team workflow.

## Type

Team type (multi-role collaboration) · Version 1.10.10 · 11 members

## Members & Naming Wordplay

| Member ID | Name | Role | Wordplay |
|-----------|------|------|----------|
| julia-dev-team-lead | Julia | Delivery Director | Pun on 「主理呀」 (*zhǔlǐya*) — the lead |
| product-manager | Remy | Product Manager | req (**re**quirement) — takes "re" |
| architect | Archie | Architect | arch (**arch**itecture) |
| engineer | Mark | Engineer | **ma**ke — the one who builds things |
| qa-engineer | Vera | QA Engineer | **ver**ify — verification incarnate |
| reverse-engineer | Tracey | Reverse Engineer | **trace** — from entry point down to the database |
| delivery-designer | Della | Delivery Designer | **de**ck / **de**liver — presentable delivery decks |
| knowledge-curator | Knox | Knowledge Curator | **kn**ow — guardian of knowledge (Fort Knox vault imagery; provenance, trust, freshness) |
| release-engineer | Ship | Release Engineer | **ship** — safely landing verified work |
| decision-advisor | Ed | Decision Advisor | a**d**visor — the first objector before costly or irreversible moves |
| ledger-liaison | Luca | Ledger Liaison | route + task card — translates ledger route cards into Julia's tasks |

## Task Types & Workflow Mapping

The lead Julia first runs **Phase 0 task analysis**, then picks one of 21 workflows; unneeded phases are skipped, never wasted.

| What you say | Task type | Workflow |
|--------------|-----------|----------|
| Build a tool / website / API | Greenfield | A Full Delivery |
| Requirements are messy, write a PRD | Requirements | B Requirements |
| Review my code | Review | C Health Check / G Security Review |
| Add a feature to an existing system | Feature | D Feature |
| This errors / output is wrong | Defect | E Defect Fix |
| Too slow / refactor this | Refactor | F Refactor |
| Add tests / raise coverage | Test backfill | H Test Backfill |
| Upgrade version / switch framework | Migration | I Migration |
| Integrate payments / login / maps API | Integration | J Integration |
| Crawler / RAG / LLM app | Data AI | K Data/AI |
| Build an XX management system ontology-driven | Ontology-driven | L Ontology End-to-End |
| Take over an old project / inventory the code | Reverse engineering | M Reverse Engineering |
| Make it a deck / briefing | Delivery narrative | N Narrative Deck |
| Draw architecture diagrams / knowledge graph | Visual modeling | O Multi-view Modeling |
| Build a knowledge base / is this number trustworthy | OKF knowledge | P OKF Knowledge |
| Reproduce first / prove it really works | Rigorous engineering | Q pstack Rigor |
| Merge PRs / pick up the last round / I'm going to sleep | Release & pickup | R Release & Session Pickup |
| Split parallel tasks / bounded loop / CI all green | Structured orchestration | S Orchestration & Bounded Loop |
| Deep review PR / security + maintainability | Deep diff review | T Deep Diff Review & Decision Review |
| Find blind spots / stuck twice / confirm before delivery | Decision review | T or direct Ed |
| Ledger integration / follow ledger routing / take a task from next_queue | Ledger | U Ledger Bridge & Controlled Writes |
| Which technology should I use | Tech consulting | B or ask Archie |

## Supported Project Types

Web frontend, backend API, full-stack, CLI/automation scripts, desktop, mobile, data processing, AI/LLM apps, database design, DevOps/deployment.

Each type has dedicated design and verification focuses, written explicitly by the lead at dispatch — e.g. APIs emphasize contracts and error codes, AI apps emphasize hallucination defense and cost, CLIs emphasize idempotency and output format.

## Optional Methodology: Ontology-Driven Modeling

The package bundles `skills/ontology-modeling/`, distilled from the open-source [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework) (by @人月聊IT, Apache-2.0). It splits business systems into **orthogonal, independently evolvable, YAML-carried** model concerns, building a traceable "requirements → design → code" chain.

**When to enable** (loaded by Archie in Phase 2):

- Mid-to-large business systems (ERP / CRM / approvals / contract management)
- Rule-dense, multi-object linkage, audit traceability needs
- Multi-role collaboration requiring stable handoff contracts

**When not to**: small tools, pure frontend, one-off scripts, exploratory AI apps — avoid over-engineering.

**Version choice**: v9 (7 models, monolith-sync, best for stable AI code generation) for actual delivery; v6 (11 models, with events/interfaces/persistence mappings) for full-picture understanding and complex integrations.

Five members are wired in: Remy annotates acceptance-to-function-point mapping, Archie produces orthogonal models, Mark maps models to code, Vera runs traceability gates. Full methodology in `skills/ontology-modeling/SKILL.md`; attribution in the same directory's `ATTRIBUTION.md`.

## Optional Pipeline: Ontology-Driven End-to-End Development

The second skill `skills/ontology-driven-dev/` is distilled from [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev) (MIT, Copyright 2026 sharptoolbox), adding the two stages around modeling:

- **Eight-stage requirement exploration**: overall understanding → business objects → functions & rules → cross-object linkage → approval flows → queries & reports → roles & permissions → UI prototype
- **Human confirmation gates**: each stage asks in a fixed format and hard-pauses for confirmation; auto-completed items are marked `[AI-autofill]`, enterprise-specific items must be confirmed, and anything `[pending]` blocks completion
- **10-step build pipeline**: from 7-model YAML to DDL, service layer, permissions, workflow engine, page routing, AI dialog (with read-only SQL safety boundary), full-chain integration and acceptance

Trigger: say "build an XX management system" or "ontology-driven development" — the lead runs **Workflow L**: Remy explores & confirms → Archie models → Mark builds `code-app/` → Vera verifies traceability.

Division of labor: `ontology-modeling` owns modeling detail; `ontology-driven-dev` owns the end-to-end pipeline. The upstream tech stack source is not embedded; fetch from the original repo when needed.

## More Capabilities: Reverse Engineering, Visual Models, Decks, Knowledge Bases

Four more methodologies were distilled from other sharptoolbox repositories, all as **optional skills** loaded on demand:

| Skill | Source / License | When to use | Members |
|-------|------------------|-------------|---------|
| `codebase-reverse` | [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) · MIT | Taking over legacy systems, pre-migration inventory, reconstructing requirements docs | Tracey (reverse) + Vera (coverage reconciliation) |
| `visual-model` | [visual-model](https://github.com/sharptoolbox/visual-model) · CC BY 4.0 | Delivery-grade architecture diagrams, SysML five views, knowledge graphs | Archie |
| `consulting-html-ppt` | [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) · No license declared | Briefings, acceptance decks, presentable materials | Della |
| `llm-knowledge-base` | [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) · MIT | RAG knowledge extraction, source-constrained QA | Mark + Vera |

### Full Integration: Open Knowledge Format (OKF)

The biggest risk of reverse-engineering docs, architecture decisions and metric definitions is **silent staleness** — the file is still there, but no longer trustworthy. This version fully integrates the three skills of [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format) (Apache-2.0, publisher: Google, v0.3):

| Skill | Responsibility |
|-------|----------------|
| `okf-format` | v0.3 spec: bundle structure, frontmatter, provenance, trust tiers, lifecycle, verifiable computation |
| `okf-generate` | Six iron rules and procedures for creating / updating / migrating / repairing / validating bundles |
| `okf-consume` | Read-only QA, reporting trust tier, status, freshness and source per concept |

The eighth member **Knox (Knowledge Curator)** leads OKF writes and queries; Vera independently re-checks trust tiers and attestations.

**Three gap-filling mechanisms**:

- **Trust tiers**: unverified / machine-confirmed / human-reviewed. Key rule: "once AI rewrites a human-reviewed concept, the human review immediately lapses" — exactly where multi-agent collaboration fools itself.
- **stale_after freshness**: expiry judged by absolute timestamps, mechanically comparable; omit when no known re-check cadence exists — never invent dates.
- **Verifiable computation**: agents can only fill parameters, never change formulas; consumers verify receipts with a deterministic attester. This upgrades hallucination defense from prompt discipline to a mechanical contract, and gives Vera's `PASS/FAIL` computable grounds.

`llm-knowledge-base` and OKF **divide labor explicitly**: the former extracts scenarios/concepts/entities from articles; the latter handles persistence, exchange and trust. Mark extracts, then Knox completes provenance and trust fields — no duplicated work. Python scripts from the original repo are not embedded; see each skill's `ATTRIBUTION.md`.

### Rigorous Engineering & Verifiable Delivery: pstack

This version distills [pstack from cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack) (by Lauren Tan, MIT, 19k stars) — one of the most popular plugins in Cursor's official library, whose core claim is "go deep to go fast" and "write less, better code". Four skills, four duties:

| Skill | Responsibility |
|-------|----------------|
| `pstack-principles` | 24 engineering principles (core / architecture / verification / delegation / meta) — what "done well" means |
| `pstack-playbooks` | 22 playbook routes: bug fix, perf, feature, shipping, session pickup |
| `pstack-verification` | Prove it works, the seven benchmark questions, project-local verification skills, formal verification, pinning errors into structure |
| `pstack-parallel-review` | swarm (split/race), arena (compete & graft strengths), interrogate (adversarial review, only run-verified findings survive) |

The ninth member **Ship (Release Engineer)**: Vera judges correctness; Ship safely lands what's right — independently verifying every PR, merging only bottom-up contiguous passing segments, cross-checking `git patch-id` so rebased verdicts still hold, touching no other branch mid-landing, stopping at the ceiling.

**The three most valuable disciplines**:

- **Every line of code traces to runtime evidence**: bug fixes must reproduce first, bisect to root cause; "might help" guards are hypotheses, not fixes; if evidence contradicts, revert.
- **The seven benchmark questions**: name the limiting factor, confirm peer calibration, do order-of-magnitude arithmetic, count errors, alternate five or more runs, measure end-to-end, confirm work actually happened. Fail any → mark inconclusive, never claim speedup.
- **Adversarial review keeps only run-verified findings**: issues without command-output proof (including style, naming, structure) are discarded; shared root causes merge; "no findings" is a valid result.

**Division of labor with existing capabilities**: `ontology-modeling` checks requirements-to-code mapping, `pstack-verification` checks actually-running behavior, OKF attestation checks whether computation receipts were tampered with — complementary. CI-specific model configs and plugin dependencies are not embedded; see each skill's `ATTRIBUTION.md`.

**Gate conflicts**: pstack says "reversible work shouldn't ask humans"; this squad's priority order is human confirmation gates > Vera `PASS` > irreversible-action confirmation > everything else, proceed directly.

**Design trade-offs**:

- **Reverse engineering is full-coverage, depth is layered**: Tracey builds the full asset ledger (B0–B9) first, then drills per feature into the database; Vera independently reconciles coverage — unattributed assets block release. Writing feature lists off incomplete baselines is the classic reverse-engineering failure.
- **Decks stay faithful to facts**: Della's pages may take four forms (real charts / architecture diagrams / structure models / text categories), but data must never be invented and every technical claim carries a source. Production starts only after Vera's `PASS`.
- **License discipline**: projects with clear licenses are condensed restatements with full attribution; `consulting-html-ppt`'s original repo **declares no license**, so only methodology points are absorbed — no templates, icons or artifacts copied; built-in or self-made templates substitute. Each skill's `ATTRIBUTION.md` keeps source and license notes.

## Further Evolution: Other High-Value cursor/plugins Projects

This version scanned the whole [cursor/plugins](https://github.com/cursor/plugins/tree/main) library and picked four groups of practices with real increments for multi-agent software delivery, all converted into **optional skills**; Cursor-specific SDK, Bun scripts, hooks and Slack integrations are never embedded — only portable methodology is kept.

| New skill | Distilled from | What it does | Members |
|-----------|----------------|--------------|---------|
| `structured-orchestration` | `orchestrate` + `ralph-loop` + `cursor-team-kit/loop-on-ci` (MIT) | Planner/Worker/Verifier boundaries, verbatim handoffs, five-tier verifier evidence, completion promises + iteration caps, failure modes & Andon, `gh pr checks` CI loop | Julia (orchestration) + Ship (CI) |
| `deep-diff-review` | `thermos` + `dyl-stack` (MIT) | Correctness/security vs structure/maintainability dual-axis parallel review, code judo / 1k-line / spaghetti rulers, dedup to max 7 pasteable comments + one traffic light | Vera + Archie, Ed re-checks major findings |
| `decision-gates` | `advisor` + `dyl-stack` (MIT) | Major-decision / stuck-twice / pre-delivery checkpoints, read-only `Verdict / Why / Recommendations / Risks / Answers / Confidence`, The Algorithm, root-cause sentence, merge & taste-veto discipline | Ed |
| `agent-friendly-cli` | `cli-for-agent` (MIT) | Non-interactive flags, layered help & examples, stdin/pipeline, actionable errors, idempotency, `--dry-run`, JSON output & exit codes | Mark + Archie |

The tenth member **Ed (Decision Advisor)**: he writes no code, opens no PRs, merges nothing — he gives a second opinion only before costly or irreversible moves. His advice never overrides human confirmation gates, Vera `PASS`, or irreversible-action confirmation — a deliberately fixed priority order.

**The four most valuable disciplines**:

- **Planner writes no code, Workers don't talk to each other, Verifier doesn't touch target source**. `orchestrate` replaces shared state with verbatim handoffs so parallel tasks converge without global coordination; downstream declares dependencies, the lead shuttles.
- **Completion requires promises and caps**. Ralph Loop iterates the same prompt, may emit a completion promise only when work is truly done; at the cap it reports honestly that it's unfinished — preventing agents from lying to close out. Verifier's `verifier-blocked` also forbids dressing environment failures as passes.
- **Deep review is dual-axis, diff-only, few and precise**. Thermos separates bug/security/devex/feature-gate from maintainability; dyl-stack compresses findings to max 7 pasteable comments plus one traffic light, never posting to PRs, never approving, never merging.
- **Question requirements, delete first, then optimize**. `The Algorithm` and `Root cause: X because Y` complete pstack's root-cause discipline: null guards, retries, sleeps, skips and snapshot updates are symptom fixes until the root-cause sentence holds.

**What was deliberately not absorbed**: `orchestrate`'s Cursor SDK / Bun CLI / Slack Andon scripts, `ralph-loop`'s hooks, `advisor`'s model bindings and state files, `thermos`' subagent definitions, `dyl-stack`'s Figma / UI judge flows — platform-bound, migration cost exceeds benefit; insights from `agent-compatibility`, `continual-learning`, `workflow-from-chats` are already covered by existing verification, knowledge and preference mechanisms.

## Optional Protocol: ledger-driven-dev Bridge

The eleventh member **Luca (Ledger Liaison)** and the skill `ledger-bridge` wire the governance capability of [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev) (MIT, Copyright 2026 Ledger-Driven Dev contributors) into Julia's execution chain. This is not a merge — it's a **read-only thin bridge**:

| Handoff object | Purpose |
|----------------|---------|
| `intent.json` | Turns plain-language requirements, non-goals, capability codes and write scopes into verifiable intent |
| `route.handoff` / `next_queue` | Get the unique expert, handoff chain and a single task card |
| `test_report` + `verify_ledger` JSON | Converts Vera's evidence into `declared / verified` and invariant results |
| `approval_bundle` / `audit` | Only prepares commands for approval; humans sign off, Ship executes |

**The ledger-driven-dev repo itself is untouched**: no schema changes, no changes to its 31 invariants, no new experts, no copying of its 24 skills. What the target project needs is one-time governance onboarding: capability codes, `verify_ledger`, agent registration and test-evidence binding.

Gate priority: **human confirmation > ledger write gate > irreversible-action confirmation > Vera `PASS` > everything else**. Luca reads, translates and prepares only; never executes writes with `--apply`, and never copies ledger JSON into julia-dev as a second source of truth. Condensed methodology in `skills/ledger-bridge/SKILL.md`; attribution in the same directory's `ATTRIBUTION.md`.

## v1.9.0: Seam Repairs

Post-integration gap re-evaluation found the problem had shifted from "capability gaps" to "seams and runnability". Five mechanisms were added without new members or workflows:

| Mechanism | Gap solved | Where |
|-----------|-----------|-------|
| **Footprint spec** | Three references to footprints with no format, no location, no owner | Lead SOP "footprint spec" + Vera/Ship/Ed MDs |
| **Single contract entry** | `intent.json` and Julia's task contract could double-write, unclear precedence | Phase 0.5 + Workflow U + ledger-bridge hard rule 8 |
| **PASS grading** | Chat-style `PASS` and ledger `verified` mixed, inflating value | Phase 4 + ledger-bridge hard rule 10; governed projects always `verified-PASS` |
| **Unblock (Andon)** | Fail-closed always "stops" but had no recovery path | ledger-bridge "unblock" section + forbidden behaviors; stuck twice → user Andon |
| **Preflight** | Bridge commands depend on the target project's installed ledger scripts; no drift check | Phase 0.5 + Workflow U + ledger-bridge "Preflight" section |

Footprint vs ledger vs OKF division fixed: **ledger = project source of truth, OKF = external knowledge trust layer, footprint = current work-site draft**; none of the three copy each other; footprints only reference the other two.

## Evolution Mechanism: Controlled Self-Evolution

Members are ephemeral per-session executors with no cross-session memory — the only evolving carrier is the expert package's documents themselves. So evolution is never free self-modification, but a six-step loop: **member proposal (requires ≥2 repetitions) → Ed read-only review → human decision (the only activation gate) → lead executes the change → validate + register + git commit → evolution log entry**.

- Proposals follow a fixed seven-part format with verifiable evidence; rule changes merge-replace, never stack
- Forbidden zones (forbidden behaviors, gate priority, member boundaries, the four handoff objects) can only be changed by the human; members may not propose changes to them
- One activation = one commit, a natural rollback point; change history in `docs/evolution-log.md`, loop rules in `skills/self-evolution/SKILL.md`

## Iteration History

All evolution comes from four channels: user decisions, gap-assessment walkthroughs, live-testing feedback, and external open-source absorption — always through the controlled loop above. The full narrative from package foundation (v1.0–v1.8.x), seam repairs (v1.9.0), live-testing feedback (v1.9.1), institutionalization (v1.10.0–1.10.2), usability (v1.10.3–1.10.5), release & governance (v1.10.6–1.10.8) to naming & docs (v1.10.9–1.10.10), including per-version sources and the lessons-learned list, is in [`docs/iteration-history.md`](iteration-history.md); per-change records in [`docs/evolution-log.md`](evolution-log.md).

## Features

- **Task routing**: type and project-shape analysis first, then workflow; bug fixes never get forced into writing PRDs
- **Structured handoffs**: stages exchange PRDs / design docs / change summaries / test reports, never verbal accounts
- **Incremental safe changes**: existing-system changes start with impact analysis, preserving backward compatibility
- **Per-shape verification**: Vera (QA) adapts testing to Web / API / data / AI; modification tasks always include regression
- **Explicit quality gates**: Vera emits `PASS`/`FAIL` with evidence; the lead never ghostwrites or softens conclusions
- **Human confirmation gates**: Workflow L's exploration asks and hard-pauses per stage, eliminating AI assumptions about enterprise-specific rules
- **Source reverse engineering**: Workflow M full baseline + feature penetration chains + coverage reconciliation, surfacing hidden features and database mappings
- **Delivery narrative**: Workflow N turns verified results into a single-file HTML deck with action-style titles
- **Trustworthy knowledge**: Workflow P's OKF bundles give every concept a source, trust tier and freshness — refusing silent staleness
- **Rigorous engineering**: Workflow Q replaces self-reporting with runtime evidence; Workflow R lands only verified contiguous segments
- **Structured orchestration**: Workflow S drives large tasks with worker/verifier handoffs and bounded loops; CI judged by `gh pr checks`
- **Deep diff review**: Workflow T dual-axis reviews diffs, outputting at most 7 pasteable comments and one traffic light; never posts to PRs, never approves
- **Decision second opinions**: Ed gives read-only verdicts at major decisions, stuck-twice moments and pre-delivery, blocking symptom fixes with The Algorithm and root-cause sentences
- **Ledger bridge**: Workflow U chains the restate gate, expert routing, task cards, evidence grading and controlled writes via Luca — no double routing, no second source of truth
- **AI dual-baseline evaluation**: Workflow K freezes golden set, version and cost budget before implementation; Phase 4 must deliver "effect + cost" together, missing either is FAIL
- **System-level security checklist**: before launch Vera runs secrets / dependency licenses / PII / permissions / threat modeling / accessibility — 🔴 unresolved blocks Ship from landing; the threat-model summary is a mandatory section of Archie's design docs
- **Environment scripts have an owner**: launch / doctor / drive / evidence scripts are maintained by Mark long-term; environment failures get scripts fixed first, never used as verification excuses
- **Controlled self-evolution**: member proposals, Ed review, human decision, lead execution; git commits are rollback points, fully traceable
- **Planning-stage first-principles decomposition**: Remy tags every requirement "hard constraint or convention" (conventions need rationale), Archie's design docs must include a fundamental-facts table (each with source); analogy-driven design is intercepted at planning
- **Switchable operator modes**: layman / standard / expert, declared at Phase 0, switchable anytime; layman mode adds plain-language summaries and behavioral acceptance checklists with opt-out delegation of technical decisions; irreversibility gates and test gates never relax in any mode
- **Layman five guardrails**: mode detection (proactively suggest switching), delegated-decision ledger (plain-language, reversible per item), plain-language handover card (location + usage + recall phrase), quick-reply questions (A/B options), "something feels off" as a valid signal
- **Collaboration iron rules**: the lead personally forms the team, all information flows through the lead, members never connect directly

## Usage Examples

- I have a development request — classify it and deliver with a suitable workflow.
- Fix this bug / add a feature / refactor this code.
- Review this code and give me test cases and a quality report.
- Migrate this old project from Python 2 to 3 with regression tests.
- Build a RAG QA app, from data spec to running code, fully delivered.
- Design a procurement approval system traceable from every requirement to its code location.
- Use ontology-driven development for a contract management system; I confirm every exploration stage.
- Take over this legacy project: reverse the full feature list, penetration chains and database tables, including cron jobs without menus.
- Turn this delivery into a 12-page consulting-style HTML deck with sourced technical claims.
- Build an OKF knowledge base and tell me which concepts are unverified or stale.
- Fix this bug rigorously: reproduce, bisect to root cause, then show me failing-to-passing output.
- These PRs are all green — verify and merge bottom-up, tell me where you stopped.
- Split this big task into workers/verifiers, run a loop with completion promises and caps, give me the handoff log.
- Deep review this PR: security and maintainability separately, max 7 pasteable comments and one traffic light.
- I'm stuck on the same error twice — have Ed read the evidence and give a second opinion after The Algorithm questions the requirement.
- Bridge this project's ledger: follow the route, take one card from next_queue for me.
- Convert Vera's test evidence into ledger `verified`, prepare the approval bundle but don't write yet.

## Avatars

Avatars are auto-generated in `avatars/`. To replace them: PNG (recommended) or JPG, 512×512 px, max 500KB each.

## Installation

Place the expert package directory under the experts directory:

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/julia-dev/
```

Then register it to make it visible:

```bash
python3 scripts/register_expert.py <expert-dir>
```

## Acknowledgments

This package is a **condensed restatement** of methodologies from the following open-source projects, not a copy of their files; each derived skill directory carries its own `ATTRIBUTION.md` with exact source and license. Upstream projects remain under their own licenses (MIT / Apache 2.0 / CC BY 4.0); thanks to all original authors:

| Source project | Author / holder | License | Distilled into |
|----------------|-----------------|---------|----------------|
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | Lauren Tan | MIT | pstack-principles / playbooks / verification / parallel-review |
| [orchestrate](https://github.com/cursor/plugins/tree/main/orchestrate), [ralph-loop](https://github.com/cursor/plugins/tree/main/ralph-loop), [cursor-team-kit](https://github.com/cursor/plugins/tree/main/cursor-team-kit) | Cursor | MIT | structured-orchestration |
| [thermos](https://github.com/cursor/plugins/tree/main/thermos), [dyl-stack](https://github.com/cursor/plugins/tree/main/dyl-stack) | Cursor / Dylan Gattey | MIT | deep-diff-review |
| [advisor](https://github.com/cursor/plugins/tree/main/advisor), dyl-stack | Cursor / Dylan Gattey | MIT | decision-gates |
| [cli-for-agent](https://github.com/cursor/plugins/tree/main/cli-for-agent) | Eric Zakariasson | MIT | agent-friendly-cli |
| [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev) | sharptoolbox | MIT | ontology-driven-dev |
| [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) | sharptoolbox | MIT | codebase-reverse |
| [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) | sharptoolbox | MIT | llm-knowledge-base |
| [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework) | sharptoolbox (@人月聊IT) | Apache 2.0 | ontology-modeling |
| [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format) | open-knowledge-format contributors (Google) | Apache 2.0 | okf-format / generate / consume |
| [visual-model](https://github.com/sharptoolbox/visual-model) | sharptoolbox | CC BY 4.0 | visual-model |
| [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) | sharptoolbox | No license declared | consulting-html-ppt (methodology points only; no templates or assets copied) |
| [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev) | iczrac | MIT | ledger-bridge + Luca role |

The `self-evolution` skill, operator modes and layman guardrails are original to this package. The package itself is released under MIT — see the root `LICENSE`.

## Multi-Platform Distribution

The WorkBuddy package is the **canonical single source of truth**; other platform bundles are generated by `python3 scripts/build_dist.py` into `dist/`, always rebuilt by script, never hand-edited. All platforms share the same iron rules: gates, test evidence, operator modes, the first-principles gate and evolution-proposal discipline.

| Distribution dir | Platform | Form | Adaptation |
|------------------|----------|------|------------|
| `dist/claude-code/` | Claude Code | **Full team** | `.claude-plugin/plugin.json` + 11 subagents + 19 skills + `/julia` command |
| `dist/agents-md/` | Codex CLI / Gemini CLI / Jules etc. | **Solo (role-switching)** | `AGENTS.md` master + `roles/` + `skills/`; a single agent wears hats per phase, Ed/Vera become self-review and run-the-tests hats |
| `dist/cursor/` | Cursor | Solo variant | `.cursor/rules/julia-dev.mdc` (`alwaysApply`) + `roles/` + `skills/` |
| `dist/copilot/` | VS Code Copilot | Custom agents | `.github/agents/` 11 agents; no auto-routing, operator explicitly coordinates via `@julia-dev-team-lead` |

Rewrite discipline: cross-platform conversion is **semantics-preserving** only (e.g. SendMessage collaboration semantics become result-return, platform-specific frontmatter cleaned); no gate, role division or methodology content changes.

## Packaging

```bash
zip -r julia-dev.zip julia-dev/
```
