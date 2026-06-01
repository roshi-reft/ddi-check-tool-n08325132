import csv

def load_data(path):
    interactions = {}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            d1 = row['drug1'].lower()
            d2 = row['drug2'].lower()
            interactions[(d1,d2)] = row
            interactions[(d2,d1)] = row
    return interactions


def check_interactions(drugs, interactions):
    results = []
    for i in range(len(drugs)):
        for j in range(i+1, len(drugs)):
            pair = (drugs[i], drugs[j])
            if pair in interactions:
                results.append(interactions[pair])
    return results


def main():
    data = load_data('data/ddi_data.csv')

    user_input = input("Enter drugs (comma separated): ")
    drugs = [d.strip().lower() for d in user_input.split(',') if d.strip()]

    results = check_interactions(drugs, data)

    if results:
        print("
Interactions found:
")
        for r in results:
            print(f"{r['drug1']} + {r['drug2']}")
            print(f"Severity: {r['severity']}")
            print(f"Recommendation: {r['recommendation']}
")
    else:
        print("No interactions found.")


if __name__ == '__main__':
    main()
