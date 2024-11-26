from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set(map(self.get_forwarding_address, emails))
        return len(unique_emails)

    def get_forwarding_address(self, address: str) -> str:
        local_name, domain_name = address.split("@")
        forwarding_local_name = local_name.replace(".", "").split("+")[0]
        return f"{forwarding_local_name}@{domain_name}"
