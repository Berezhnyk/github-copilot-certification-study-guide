# GitHub Copilot Certification Practice Test 2
## Advanced Features and Enterprise Usage

**Time Limit: 45 minutes**  
**Total Questions: 30**  
**Passing Score: 80% (24 correct answers)**

---

### Question 1
What is the primary advantage of GitHub Copilot Business over GitHub Copilot Individual?

A) Faster code suggestions  
B) More programming languages supported  
C) Enterprise-grade privacy and security features  
D) Better integration with VS Code  

**Answer: C**  
**Explanation:** GitHub Copilot Business provides enterprise-grade privacy features, including no training on business data, audit logs, and administrative controls.

---

### Question 2
Which file would you create to exclude specific patterns from GitHub Copilot suggestions?

A) `.copilot-ignore`  
B) `.github/copilot-exclusions.yml`  
C) `copilot-config.json`  
D) `.copilotignore`  

**Answer: B**  
**Explanation:** The `.github/copilot-exclusions.yml` file is used to configure content exclusions at the repository level.

---

### Question 3
What does the following comment accomplish in your code?
```python
# copilot:disable-next-line
secret_key = "sk-1234567890abcdef"
```

A) Prevents Copilot from suggesting similar patterns  
B) Excludes the next line from Copilot training data  
C) Disables Copilot for the entire file  
D) Marks the line as sensitive data  

**Answer: B**  
**Explanation:** The `copilot:disable-next-line` comment excludes the immediately following line from being used in Copilot's training data and suggestions.

---

### Question 4
In GitHub Copilot Chat, which prompt would be MOST effective for generating unit tests?

A) "write tests"  
B) "generate unit tests for this function with edge cases and mocking"  
C) "test this code"  
D) "make tests for function"  

**Answer: B**  
**Explanation:** Specific, detailed prompts that include context like "edge cases and mocking" produce better, more comprehensive results.

---

### Question 5
What is the maximum context window that GitHub Copilot typically considers when making suggestions?

A) Current line only  
B) Current function  
C) Current file plus recently opened files  
D) Entire project directory  

**Answer: C**  
**Explanation:** Copilot considers the current file and recently opened files to provide contextually relevant suggestions.

---

### Question 6
Which keyboard shortcut accepts a GitHub Copilot suggestion in VS Code?

A) Ctrl+Enter (Cmd+Enter on Mac)  
B) Tab  
C) Ctrl+Space (Cmd+Space on Mac)  
D) Enter  

**Answer: B**  
**Explanation:** The Tab key is the standard shortcut to accept a Copilot suggestion in VS Code.

---

### Question 7
What happens when you enable "public code suggestions" in GitHub Copilot settings?

A) Your code becomes publicly available  
B) Copilot can suggest code similar to public repositories  
C) All suggestions are based only on open source code  
D) Copilot shares your code with other users  

**Answer: B**  
**Explanation:** When enabled, Copilot can suggest code that might be similar to publicly available code repositories.

---

### Question 8
In a team environment, how should you handle Copilot suggestions that might contain hardcoded secrets?

A) Use them as-is since Copilot filters secrets  
B) Always review suggestions and replace with environment variables  
C) Disable Copilot in security-sensitive files  
D) Report the suggestions to GitHub  

**Answer: B**  
**Explanation:** Always review suggestions and replace any hardcoded values with secure alternatives like environment variables.

---

### Question 9
Which of the following is NOT a valid way to provide context to GitHub Copilot?

A) Writing descriptive comments  
B) Using meaningful variable names  
C) Including example inputs/outputs in comments  
D) Adding random text to increase file size  

**Answer: D**  
**Explanation:** Random text doesn't provide meaningful context. Copilot works best with clear, descriptive code and comments.

---

### Question 10
What is the recommended approach when Copilot suggests code that you don't fully understand?

A) Accept it anyway since Copilot is usually correct  
B) Reject it and write the code manually  
C) Research and understand the suggestion before accepting  
D) Modify it randomly until it works  

**Answer: C**  
**Explanation:** Always understand code before accepting it. This ensures code quality and helps you learn.

---

### Question 11
In GitHub Copilot for Business, audit logs capture:

A) Only accepted suggestions  
B) All suggestions shown to users  
C) User engagement data and policy violations  
D) Source code from suggestions  

**Answer: C**  
**Explanation:** Audit logs track user engagement, policy compliance, and security events, not the actual code content.

---

### Question 12
Which prompt engineering technique is MOST effective for generating database queries?

A) "write SQL"  
B) "SELECT * FROM table"  
C) "Write a SQL query to find all users who registered in the last 30 days, include their email and registration date"  
D) "database query needed"  

**Answer: C**  
**Explanation:** Specific prompts with clear requirements (timeframe, fields needed) generate more accurate and useful queries.

---

### Question 13
What is the primary purpose of GitHub Copilot's content filtering?

A) Improve code quality  
B) Prevent copyright violations  
C) Filter out sensitive data and inappropriate content  
D) Reduce suggestion response time  

**Answer: C**  
**Explanation:** Content filtering helps prevent suggestions containing sensitive data, secrets, or inappropriate content.

---

### Question 14
In which scenario should you use GitHub Copilot Chat instead of inline suggestions?

A) Simple code completion  
B) Explaining complex algorithms or debugging issues  
C) Variable name suggestions  
D) Syntax correction  

**Answer: B**  
**Explanation:** Copilot Chat is ideal for explanations, debugging help, and complex problem-solving conversations.

---

### Question 15
What does GDPR compliance mean for GitHub Copilot users?

A) Code suggestions are stored indefinitely  
B) Users have rights to access, correct, and delete their data  
C) All European users must use Copilot Business  
D) Code is automatically shared with EU authorities  

**Answer: B**  
**Explanation:** GDPR provides users with rights over their personal data, including access, rectification, and erasure rights.

---

### Question 16
Which comment style provides the BEST context for Copilot suggestions?

A) `// TODO: fix this`  
B) `// Calculate the monthly payment for a loan given principal, interest rate, and term in years`  
C) `// This is important`  
D) `// Code goes here`  

**Answer: B**  
**Explanation:** Detailed, descriptive comments that explain the purpose and requirements help Copilot generate better suggestions.

---

### Question 17
In a multi-file project, how does Copilot understand relationships between files?

A) By analyzing import statements and recently opened files  
B) By scanning the entire project directory  
C) By reading the README file  
D) It doesn't consider other files  

**Answer: A**  
**Explanation:** Copilot analyzes imports, dependencies, and recently opened files to understand project context.

---

### Question 18
What is the recommended practice for using Copilot with test-driven development (TDD)?

A) Write tests after implementation  
B) Let Copilot write both tests and implementation  
C) Write failing tests first, then use Copilot for implementation  
D) Avoid using Copilot for testing  

**Answer: C**  
**Explanation:** TDD best practice is to write failing tests first, then use Copilot to help implement the functionality to make tests pass.

---

### Question 19
Which organization setting would prevent Copilot from using public code patterns in suggestions?

A) `public_code_suggestions: false`  
B) `allow_public_code: false`  
C) `block_public_suggestions: true`  
D) `private_mode: true`  

**Answer: A**  
**Explanation:** Setting `public_code_suggestions` to false prevents Copilot from suggesting code similar to public repositories.

---

### Question 20
When should you manually exclude content using `copilot:disable` comments?

A) Never, rely on automatic filtering  
B) For any proprietary algorithms or sensitive business logic  
C) Only for password variables  
D) For all database-related code  

**Answer: B**  
**Explanation:** Manual exclusions should be used for proprietary algorithms, sensitive business logic, or confidential information.

---

### Question 21
What is the correct syntax to disable Copilot for an entire code block?

A) `// copilot:disable-block`  
B) `/* copilot:disable-start */ ... /* copilot:disable-end */`  
C) `// copilot:disable-start` ... `// copilot:disable-end`  
D) `// copilot:off` ... `// copilot:on`  

**Answer: C**  
**Explanation:** Use `// copilot:disable-start` and `// copilot:disable-end` comments to exclude entire code blocks.

---

### Question 22
In enterprise environments, what is the recommended approach for handling Copilot-generated code in security-critical applications?

A) Trust Copilot completely  
B) Disable Copilot entirely  
C) Review all suggestions through security and code review processes  
D) Only use suggestions for non-critical features  

**Answer: C**  
**Explanation:** All code, including Copilot suggestions, should go through proper security review and code review processes.

---

### Question 23
Which type of data does GitHub Copilot NOT collect?

A) Suggestion acceptance rates  
B) Complete source code files  
C) Error messages and diagnostics  
D) Feature usage patterns  

**Answer: B**  
**Explanation:** Copilot doesn't collect complete source files, only the necessary context for generating suggestions.

---

### Question 24
What is the primary benefit of using descriptive function and variable names when working with Copilot?

A) Faster code execution  
B) Better context understanding leading to more accurate suggestions  
C) Reduced memory usage  
D) Improved IDE performance  

**Answer: B**  
**Explanation:** Descriptive names provide better context, helping Copilot understand your intent and generate more accurate suggestions.

---

### Question 25
In GitHub Copilot Chat, what does the `/explain` command do?

A) Explains how Copilot works  
B) Provides detailed explanation of selected code  
C) Shows keyboard shortcuts  
D) Explains the current project structure  

**Answer: B**  
**Explanation:** The `/explain` command in Copilot Chat provides detailed explanations of selected code snippets.

---

### Question 26
Which practice BEST demonstrates responsible AI usage with Copilot?

A) Accepting all suggestions without review  
B) Using suggestions only for boilerplate code  
C) Understanding, reviewing, and testing all accepted suggestions  
D) Sharing all suggestions with team members  

**Answer: C**  
**Explanation:** Responsible AI usage involves understanding, reviewing, and testing all code before implementation.

---

### Question 27
What should you do if Copilot suggests code that appears to violate your organization's coding standards?

A) Accept it and fix it later  
B) Report it as a bug to GitHub  
C) Reject the suggestion and follow your organization's standards  
D) Use it but don't tell anyone  

**Answer: C**  
**Explanation:** Always prioritize your organization's coding standards and best practices over AI suggestions.

---

### Question 28
In terms of intellectual property, who owns the code generated by GitHub Copilot?

A) GitHub/Microsoft  
B) OpenAI  
C) The developer who accepts the suggestion  
D) It's shared ownership  

**Answer: C**  
**Explanation:** The developer who accepts and implements Copilot suggestions owns the resulting code, subject to applicable licenses.

---

### Question 29
What is the recommended way to handle Copilot suggestions in open source projects?

A) Always accept them since they're from AI  
B) Review for license compatibility and code quality  
C) Avoid using Copilot in open source  
D) Use them only for documentation  

**Answer: B**  
**Explanation:** Review suggestions for license compatibility, code quality, and alignment with project goals and standards.

---

### Question 30
Which metric is MOST important for measuring Copilot effectiveness in a development team?

A) Number of suggestions generated  
B) Speed of code completion  
C) Developer productivity and code quality improvements  
D) Percentage of suggestions accepted  

**Answer: C**  
**Explanation:** The most important metrics are overall developer productivity gains and improvements in code quality and delivery speed.

---

## Scoring Guide

**Excellent (27-30 correct)**: Ready for certification exam  
**Good (24-26 correct)**: Review weak areas and retake  
**Fair (18-23 correct)**: Additional study needed  
**Needs Improvement (< 18 correct)**: Comprehensive review required

## Areas to Review Based on Incorrect Answers

- **Questions 1-10**: Basic features and usage
- **Questions 11-20**: Enterprise features and security
- **Questions 21-30**: Advanced usage and best practices

## Next Steps

1. Review study materials for any missed topics
2. Practice with advanced exercises
3. Take Practice Test 3 for final preparation
4. Schedule your official certification exam
