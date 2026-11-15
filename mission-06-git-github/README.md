# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master collaborative distributed version control using Git and GitHub. This encompasses:
1. Understanding the core Git lifecycle: working directory, staging area (index), and commit repository history.
2. Creating and isolating features on a dedicated Git branch (`update-about`).
3. Updating documentation on the feature branch, committing changes, and publishing the branch to GitHub.
4. Exploring Pull Requests (PRs), code review mechanics, branch merging, and explaining how branches protect production code in team environments.
5. Building a comprehensive, one-line technical glossary of essential Git operations.

---

## 2. Work completed
- **Task 6.1 (Git Workflow Mechanics)**: Documented the basic Git workflow table and articulated the fundamental architectural distinction between staging changes with `git add` and committing snapshots with `git commit`.
- **Task 6.2 (Feature Branching)**: Created a new branch named `update-about` using `git checkout -b update-about`. Updated the root [README.md](../README.md) by adding a dedicated `## My Learning` section with four reflective insights. Staged the file, committed the changes with a clear message, and published the branch to GitHub using `git push -u origin update-about`.
- **Task 6.3 (Pull Request & Merge Simulation)**: Generated the Pull Request workflow between `update-about` and `main` (`https://github.com/Harshit-2208/digital-detective-8450/pull/new/update-about`), completed the merge into `main`, and synchronized local and remote tracking branches.
- **Task 6.4 (Git Glossary)**: Formulated concise, original one-line definitions for all nine essential Git commands.
- **Documentation**: Completed this `README.md` following the mandatory 8-section template.

---

## 3. Commands / tools used
| Command | Arguments / Flags | Purpose |
| :--- | :--- | :--- |
| `git status` | default | Inspected the working tree, staging index, and branch tracking status. |
| `git add` | `README.md` | Staged changes from the working tree into the Git staging area. |
| `git commit` | `-m "<message>"` | Created a permanent, cryptographically hashed commit snapshot. |
| `git log` | `--oneline --graph` | Inspected recent repository commit history and branch merges. |
| `git checkout` | `-b update-about` | Created and switched to the new `update-about` branch. |
| `git push` | `-u origin <branch>` | Uploaded local branch commits to the remote GitHub repository. |
| `git merge` | `--no-ff update-about` | Integrated commits from the feature branch into `main`. |

---

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

#### Git Workflow Table
| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Queries the repository index and working tree to report which files have been modified, untracked, staged for the next commit, or if the local branch is ahead/behind remote. |
| **Stage selected changes (`git add`)** | Selects and moves specific modified or newly created files from the working directory into the staging area (index), preparing them to be included in the next snapshot. |
| **Create a commit (`git commit`)** | Permanently records the currently staged snapshot into the repository's cryptographic version history, attaching a descriptive commit message, author name, timestamp, and SHA hash. |
| **View commit history (`git log`)** | Displays a chronological list of historical commits in the repository, showing commit hashes, author details, dates, and commit summaries. |

#### Difference Between Staging and Committing
- **Staging (`git add`)** acts as a flexible preparation workbench (the index). When you edit files in your working directory, they are not automatically part of version history. Staging lets you selectively handpick exactly which files, or even which specific lines, belong together in a logical milestone. Staging has no permanent commit hash and can be freely modified or unstaged.
- **Committing (`git commit`)**, by contrast, is a permanent save checkpoint. It freezes the staged contents into an immutable snapshot object in the `.git` database. Once committed, that version cannot be silently altered without changing its SHA-1/SHA-256 hash, creating a dependable restore point.

---

### Task 6.2 — Create and use a branch
- **Branch Creation**: Executed `git checkout -b update-about` to diverge from `main`.
- **Modifications**: Added the `## My Learning` section to the root `README.md`, detailing reflections on IPOS hardware interaction, CLI piping, data representations, and version control discipline.
- **Commit**: Staged with `git add README.md` and committed with the descriptive message:
  ```text
  [update-about bb3f306] Add My Learning section to root README
  ```
- **Remote Publishing**: Published the branch upstream to GitHub:
  ```bash
  git push -u origin update-about
  ```
  GitHub confirmed upstream tracking:
  `* [new branch] update-about -> update-about`

---

### Task 6.3 — Create a Pull Request

#### What is a Branch?
A **branch** in Git is an independent, lightweight pointer to a specific commit in the repository's history graph. Branches allow developers to diverge from the primary production codebase (`main`) to experiment, write new features, or fix bugs in complete isolation without disrupting the stable application or interfering with teammates' code.

#### What is a Pull Request (PR)?
A **Pull Request** is a collaborative workflow mechanism hosted on platforms like GitHub. It serves as a formal proposal to take code developed on a feature branch and merge it into a target branch (such as `main`). A PR provides a web interface where team members can review line-by-line diffs, leave inline comments, run automated continuous integration (CI) tests, discuss design decisions, and request improvements before code is approved.

#### Why Branches and PRs are Essential in Team Projects:
1. **Protection of Production Code**: The `main` branch remains clean, deployable, and bug-free because untested code cannot be pushed directly to it.
2. **Parallel Development Without Conflicts**: Multiple engineers can build separate features simultaneously on distinct branches without overwriting each other's work.
3. **Peer Review & Quality Assurance**: PRs enforce a code review culture where at least one other engineer verifies correctness and coding standards before changes enter production.

#### Activity & Merge Status:
- Branch URL on GitHub: [https://github.com/Harshit-2208/digital-detective-8450/tree/update-about](https://github.com/Harshit-2208/digital-detective-8450/tree/update-about)
- PR Comparison URL: [https://github.com/Harshit-2208/digital-detective-8450/pull/new/update-about](https://github.com/Harshit-2208/digital-detective-8450/pull/new/update-about)
- Branch Merge: Merged into `main` via `git merge update-about` and pushed upstream to GitHub (`3fc78af`).

---

### Task 6.4 — Git command glossary
1. **Initialise a repository (`git init`)**: Transforms an ordinary directory into a Git-tracked version control repository by creating the hidden `.git` metadata store.
2. **Check status (`git status`)**: Displays the current state of the working directory and staging area, highlighting untracked, modified, and staged files.
3. **Stage changes (`git add`)**: Adds working directory changes to the staging index in preparation for the next commit snapshot.
4. **Commit changes (`git commit`)**: Records the staged files as an immutable snapshot in the repository's permanent history with a descriptive log message.
5. **View history (`git log`)**: Outputs a chronological audit log of all completed commits, author details, dates, and commit messages.
6. **Create or list branches (`git branch`)**: Lists all local repository branches or creates a new pointer to the current commit without switching to it.
7. **Switch branches (`git checkout` / `git switch`)**: Moves the `HEAD` pointer and updates files in the working directory to match the target branch or commit.
8. **Publish changes (`git push`)**: Transmits local branch commits over the network to update the matching remote repository on GitHub.
9. **Retrieve remote changes (`git pull`)**: Fetches latest commits from the remote server and merges them into the current active local branch.

---

## 5. Difficulties faced
- **Understanding Branch Pointers**: Realizing that creating a branch in Git does not duplicate project files on disk, but simply creates a 41-byte pointer to a commit hash.
- **Merge Commit Graphs**: Visualizing how fast-forward merges differ from recursive/three-way merge commits that retain explicit merge history.

---

## 6. How I resolved them
- **Inspected Commit Logs**: Used `git log --graph --oneline --all` to visually trace the branch bifurcation, feature commit, and convergence back into `main`.
- **Verified Remote State**: Checked branch references on GitHub to confirm both `main` and `update-about` branches exist in the remote repository.

---

## 7. Evidence / files
- Mission 6 Documentation: [mission-06-git-github/README.md](README.md)
- Updated Root Documentation: [README.md](../README.md)
- Feature Branch: `update-about` (visible on GitHub)

---

## 8. Commit details
- **Commit Message**: `Complete Git and GitHub collaboration mission`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
