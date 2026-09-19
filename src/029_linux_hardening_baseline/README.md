# Day 029 — Linux Hardening Baseline

## Objective
Build and understand **Linux Hardening Baseline** using Ansible.

## Files
- `site.yml` — executable Ansible playbook
- `inventory` — isolated lab inventory
- `README.md` — implementation guidance

## Safe execution

```bash
ansible-playbook --syntax-check -i inventory site.yml
ansible-playbook --check -i inventory site.yml
ansible-playbook -i inventory site.yml
```

The default inventory targets localhost for safe learning. Replace it with a disposable VM or AWS host for real remote scenarios.

## Engineering checklist
- Prefer idempotent modules.
- Keep secrets in Ansible Vault/CI secrets.
- Use variables instead of hard-coded environment values.
- Use handlers for service restarts.
- Test with check mode.
- Run ansible-lint.
- Design rollback/recovery.

## Interview questions
1. Why Ansible instead of Bash?
2. What makes a task idempotent?
3. What are inventories, variables, handlers and roles?
4. How would you manage secrets?
5. How would you test Ansible in CI/CD?
6. How would you handle partial failure?
