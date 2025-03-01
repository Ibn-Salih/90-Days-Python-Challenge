# Topics:
# - Learn about dnspython in python.
# - Project:
# - Create a DNS lookup tool.

import dns.resolver

def dns_lookup(domain, record_type='A'):
    """
    Perform a DNS lookup for a given domain and record type.
    Supported record types: A, AAAA, MX, NS, TXT, CNAME
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return answers
    except dns.resolver.NoAnswer:
        return f"No {record_type} record found for {domain}"
    except dns.resolver.NXDOMAIN:
        return f"The domain {domain} does not exist"
    except dns.resolver.Timeout:
        return "DNS query timed out"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    domain = input("Enter the domain (e.g., google.com): ").strip()
    record_type = input("Enter the record type (A, MX, NS, etc.): ").strip().upper()
    
    result = dns_lookup(domain, record_type)
    
    if isinstance(result, dns.resolver.Answer):
        print(f"\n{record_type} records for {domain}:")
        for record in result:
            print(record)
    else:
        print(result)

if __name__ == "__main__":
    main()