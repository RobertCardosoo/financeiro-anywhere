CREATE DATABASE FINANCEIRO_ANYWHERE;

CREATE TABLE ANY_WALLET (ANY_WAL_ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                         ANY_WAL_USR INT UNIQUE NOT NULL,
                         );

CREATE TABLE ANY_CARD (ANY_CAR_ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                       ANY_CAR_TIPO VARCHAR(1) /*C - CRÉDITO / D - DÉBITO*/ NOT NULL,
                       ANY_CAR_NUMERO VARCHAR(16) NOT NULL,
                       ANY_CAR_FLAG TEXT NOT NULL,
                       ANY_CAR_NACIONALIDADE VARCHAR(1) NOT NULL /*N - NACIONAL / I - INTERNACIONAL*/,
                       ANY_CAR_TITULAR VARCHAR(100) NOT NULL,
                       ANY_CAR_CPF VARCHAR(11) NOT NULL,
                       ANY_CAR_ATIVO BOOLEAN DEFAULT True NOT NULL,
                       ANY_WAL_ID INT NOT NULL,
                       FOREIGN KEY (ANY_WAL_ID) REFERENCES ANY_WALLET(ANY_WAL_ID));

CREATE TABLE ANY_TRANSACOES_INTERNAS (ANY_TRA_ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                      ANY_TRA_VALOR DECIMAL(9,2) NOT NULL,
                                      ANY_TRA_TIPO VARCHAR(1) NOT NULL /* V -  A VISTA / P - PARCELADO */,
                                      ANY_TRA_NUM_PARCELAS INT DEFAULT 1 not null,
                                      ANY_TRA_REGISTRO DATETIME DEFAULT current_timestamp() Not Null,
                                      ANY_TRA_OPERACAO VARCHAR(1) NOT NULL,
                                      ANY_CARD_ID INT NOT NULL,
                                      FOREIGN KEY (ANY_CARD_ID) REFERENCES ANY_CARD(ANY_CARD_ID)
                                      );