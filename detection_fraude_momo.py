# ==============================================
# PROJET : DETECTION DE FRAUDE - MTN MoMo
# ==============================================

import datetime

transactions = []
comptes = {}

def verifier_fraude(expediteur, montant, destinataire):
    heure_actuelle = datetime.datetime.now().hour
    alertes = []
    
    if montant > 200000:
        alertes.append("⚠️ Montant très élevé")
    if heure_actuelle < 5 or heure_actuelle >= 23:
        alertes.append("⚠️ Transaction à heure suspecte")
    if destinataire not in comptes:
        comptes[destinataire] = "nouveau"
        alertes.append("⚠️ Compte destinataire nouveau")
    if comptes.get(destinataire) == "suspect":
        alertes.append("🚨 Destinataire suspect")
    
    return alertes

def effectuer_transaction(expediteur, montant, destinataire):
    print("-" * 50)
    print(f"📤 De: {expediteur}  |  📥 Vers: {destinataire}")
    print(f"💰 Montant: {montant:,} FCFA")
    
    alertes = verifier_fraude(expediteur, montant, destinataire)
    
    if alertes:
        print("\n🚨 ALERTES:")
        for a in alertes:
            print(f"   {a}")
        if len(alertes) >= 2:
            print("❌ BLOQUÉ - FRAUDE CONFIRMÉE")
        else:
            print("⚠️ Autorisé - Surveillance")
    else:
        print("✅ Transaction NORMALE")
    
    transactions.append({"statut": "valide" if not alertes else "attention"})
    return True

# ==============================================
print("=" * 50)
print("       DETECTION DE FRAUDE - MTN MoMo")
print("=" * 50)
print()

effectuer_transaction("Dupont", 15000, "Marie")
print()
effectuer_transaction("Paul", 500000, "CompteNeuf123")
print()
effectuer_transaction("Alice", 3000, "Marie")

print("\n" + "=" * 50)
print(f"📊 Total: {len(transactions)} transactions")
print("=" * 50)

