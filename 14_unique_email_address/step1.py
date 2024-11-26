from typing import List
from collections import defaultdict


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set([])

        for email in emails:
            forwarding_address = self.get_forwarding_address(email)
            unique_emails.add(forwarding_address)

        return len(unique_emails)

    def get_forwarding_address(self, address: str) -> str:
        local_name, domain_name = self.divide_address_into_parts(address)
        forwarding_local_name = self.remove_dots_from_local_name(
            self.cut_off_after_plus_mark_from_local_name(local_name)
        )
        return forwarding_local_name + "@" + domain_name

    def remove_dots_from_local_name(self, local_name: str) -> str:
        return local_name.replace(".", "")

    def cut_off_after_plus_mark_from_local_name(self, local_name: str) -> str:
        return local_name.split("+")[0]

    def divide_address_into_parts(self, address: str) -> tuple[str, str]:
        parts = address.split("@")
        return (parts[0], parts[1])
