## How to contribute to Factor Lake

### Git Basics

The Quebec team follows the standard git workflow to manage this repository. Beginners will find the steps detailed below helpful in making their first contributions.

1. Clone Repository

```
git clone https://github.com/mbh226/Factor-Lake.git
```

2. Move to repository directory 

```
cd Factor-Lake
```

3. Check status and confirm its up to date.

```
git status
```

4. Create a new branch.

```
git checkout -b <new branch>
```

5. Check that you're working in the newly created branch.

```
git branch
```

The branch your working on will be marked with an asterisk.

6. Add a new file or make changes to an existing file using VSCode or preferred editor.

7. Stage file for next commit.

```
git add <filename>
```
8. Commit changes with descriptive message.

```
git commit -m "Added new file and this is my descriptive message."
```

9. Push changes to repository branch.

```
git push origin <branch you created in step 4>
```
### Diagram System Breakdown
<details>
<summary>Portfolio Use Case Diagram</summary>

  ![Portfolio Use Case Diagram](./Diagrams/build_portfolio_use_case_042025.drawio.svg)

</details>

</details>
<summary>Included Classes Diagram</summary>
![Class Diagram](./Diagrams/class_diagram_042025.drawio.svg)

</details>

</details>
<summary>Deployment Diagram</summary>

![Deployment Diagram](./diagrams/deployment_042025.drawio.svg)

</details>

### SecDevOps Approach
The Factor Lake team has agreed to take a SecDevOps approach to our project's development and all contributors are expected to do the same. SecDevOps is a software development approach that prioritizes security.[^1] All contributors must abide by Factor Lake's Secure Coding Standard.

[^1]: https://www.pluralsight.com/blog/software-development/secdevops#:~:text=with%20Pluralsight%20Flow-,What%20is%20SecDevOps?,vulnerabilities%20they%20missed%20earlier%20on
