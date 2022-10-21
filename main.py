from symbol_table import SymbolTable


if __name__ == "__main__":
    st: SymbolTable = SymbolTable()

    assert not st.contains("abc")
    assert not st.contains('"abc"')

    st.insert("abc")
    assert st.contains("abc")
    assert not st.contains('"abc"')

    st.insert('"abc"')
    assert st.contains("abc")
    assert st.contains('"abc"')
