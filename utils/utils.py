def formata_preco(val):
    return f"R$ {val:.2f}".replace(".", ",")


# Calculate total quantity in cart
def cart_total_qtd(carrinho):
    return sum([item["quantidade"] for item in carrinho.values()])


def cart_totals(carrinho):
    return sum(
        [
            item.get("preco_quantitativo_promocional")
            if item.get("preco_quanitativo_promocional")
            else item.get("preco_quantitativo")
            for item in carrinho.values()
        ]
    )
