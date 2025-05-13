# 🧠 Dicionário Distribuído com Hprose em Python

Este projeto é uma implementação de um serviço de **dicionário distribuído** usando **Python** e **Hprose** como mecanismo de RPC (Remote Procedure Call). O servidor permite que múltiplos clientes atualizem, consultem e removam entradas de forma concorrente, com controle de acesso por `threading.Lock`.

## 📌 Descrição da Atividade

Atividade prática da disciplina de **Programação Distribuída**, com o objetivo de desenvolver um sistema baseado em objetos distribuídos.

- As **chaves** do dicionário são `string`
- Os **valores** são números inteiros positivos
- A comunicação entre cliente e servidor é feita via Hprose
- As regiões críticas do código são protegidas por `threading.Lock`, garantindo **exclusão mútua**
