# StackSense Security Specification

## Data Invariants
- A Notification must have a valid `userId` (or be global).
- An AuditLog entry cannot be deleted or modified once created.
- User data can only be modified by the user themselves or an admin.
- Leads can be managed by any authenticated user with a 'founder' or 'admin' role.

## The Dirty Dozen Payloads (Rejection Targets)
1. **Identity Spoofing**: Attempt to create a UserProfile with a different `uid` than `request.auth.uid`.
2. **Privilege Escalation**: Attempt to update own `role` from 'viewer' to 'admin'.
3. **Ghost Fields**: Attempt to add `isSuperAdmin: true` to a UserProfile during update.
4. **Invalid Type**: Attempt to set `status` in an Integration to a number instead of an enum string.
5. **Orphaned Notification**: Create a notification for a non-existent `userId`.
6. **Improper Ownership**: User A attempts to update User B's Integration config.
7. **Audit Tampering**: Attempt to delete an AuditLog entry.
8. **Resource Poisoning**: Use a 2MB string for a lead's `notes`.
9. **State Shortcutting**: Change a lead's `status` directly to 'Lost' without going through mandatory intermediate states (if enforced).
10. **Query Scraping**: Authenticated user attempts a blanket `list` on `/leads` without being a 'founder'.
11. **Timestamp Forgery**: Attempt to manual set `createdAt` instead of using `serverTimestamp()`.
12. **PII Leakage**: Attempt to read all `UserProfile` documents globally as a standard user.

## Test Runner (Draft)
```typescript
// firestore.rules.test.ts
// ... test cases for each payload above ...
```
