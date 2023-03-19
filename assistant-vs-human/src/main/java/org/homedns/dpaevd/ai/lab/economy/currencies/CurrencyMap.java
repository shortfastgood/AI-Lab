/*
 * @(#)INSTANCE.java 2023.1
 *
 * Copyright (c) 2023 by DPAEVD
 * All rights reserved
 */
package org.homedns.dpaevd.ai.lab.economy.currencies;

import java.util.HashMap;

/**
 * Generated using (<a href="https://chat.openai.com">ChatGPT 3.5</a>) using the command:
 * <pre>
 * Generate a Java map containing the ISO 4217 currency code as key and the
 * currency name as value, I need all the ISO codes, but please don't generate
 * comments, I need only the  Java code.
 * </pre>
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
public class CurrencyMap extends HashMap<String, String> {

    public static final CurrencyMap INSTANCE = new CurrencyMap();

    static {
        INSTANCE.put("AED", "United Arab Emirates Dirham");
        INSTANCE.put("AFN", "Afghan Afghani");
        INSTANCE.put("ALL", "Albanian Lek");
        INSTANCE.put("AMD", "Armenian Dram");
        INSTANCE.put("ANG", "Netherlands Antillean Guilder");
        INSTANCE.put("AOA", "Angolan Kwanza");
        INSTANCE.put("ARS", "Argentine Peso");
        INSTANCE.put("AUD", "Australian Dollar");
        INSTANCE.put("AWG", "Aruban Florin");
        INSTANCE.put("AZN", "Azerbaijani Manat");
        INSTANCE.put("BAM", "Bosnia-Herzegovina Convertible Mark");
        INSTANCE.put("BBD", "Barbadian Dollar");
        INSTANCE.put("BDT", "Bangladeshi Taka");
        INSTANCE.put("BGN", "Bulgarian Lev");
        INSTANCE.put("BHD", "Bahraini Dinar");
        INSTANCE.put("BIF", "Burundian Franc");
        INSTANCE.put("BMD", "Bermudan Dollar");
        INSTANCE.put("BND", "Brunei Dollar");
        INSTANCE.put("BOB", "Bolivian Boliviano");
        INSTANCE.put("BRL", "Brazilian Real");
        INSTANCE.put("BSD", "Bahamian Dollar");
        INSTANCE.put("BTC", "Bitcoin");
        INSTANCE.put("BTN", "Bhutanese Ngultrum");
        INSTANCE.put("BWP", "Botswanan Pula");
        INSTANCE.put("BYN", "Belarusian Ruble");
        INSTANCE.put("BYR", "Belarusian Ruble (pre-2016)");
        INSTANCE.put("BZD", "Belize Dollar");
        INSTANCE.put("CAD", "Canadian Dollar");
        INSTANCE.put("CDF", "Congolese Franc");
        INSTANCE.put("CHF", "Swiss Franc");
        INSTANCE.put("CLF", "Chilean Unit of Account (UF)");
        INSTANCE.put("CLP", "Chilean Peso");
        INSTANCE.put("CNH", "Chinese Yuan (Offshore)");
        INSTANCE.put("CNY", "Chinese Yuan");
        INSTANCE.put("COP", "Colombian Peso");
        INSTANCE.put("CRC", "Costa Rican Colón");
        INSTANCE.put("CUC", "Cuban Convertible Peso");
        INSTANCE.put("CUP", "Cuban Peso");
        INSTANCE.put("CVE", "Cape Verdean Escudo");
        INSTANCE.put("CZK", "Czech Koruna");
        INSTANCE.put("DJF", "Djiboutian Franc");
        INSTANCE.put("DKK", "Danish Krone");
        INSTANCE.put("DOP", "Dominican Peso");
        INSTANCE.put("DZD", "Algerian Dinar");
        INSTANCE.put("EGP", "Egyptian Pound");
        INSTANCE.put("ERN", "Eritrean Nakfa");
        INSTANCE.put("ETB", "Ethiopian Birr");
        INSTANCE.put("EUR", "Euro");
        INSTANCE.put("FJD", "Fijian Dollar");
        INSTANCE.put("FKP", "Falkland Islands Pound");
        INSTANCE.put("GBP", "British Pound Sterling");
        INSTANCE.put("GEL", "Georgian Lari");
        INSTANCE.put("GHS", "Ghanaian Cedi");
        INSTANCE.put("GIP", "Gibraltar Pound");
        INSTANCE.put("GMD", "Gambian Dalasi");
        INSTANCE.put("GNF", "Guinean Franc");
        INSTANCE.put("GTQ", "Guatemalan Quetzal");
        INSTANCE.put("GYD", "Guyanaese Dollar");
        INSTANCE.put("HKD", "Hong Kong Dollar");
        INSTANCE.put("HNL", "Honduran Lempira");
        INSTANCE.put("HRK", "Croatian Kuna");
        INSTANCE.put("HTG", "Haitian Gourde");
        INSTANCE.put("HUF", "Hungarian Forint");
        INSTANCE.put("IDR", "Indonesian Rupiah");
        INSTANCE.put("ILS", "Israeli New Shekel");
        INSTANCE.put("INR", "Indian Rupee");
        INSTANCE.put("IQD", "Iraqi Dinar");
        INSTANCE.put("IRR", "Iranian Rial");
        INSTANCE.put("ISK", "Icelandic Króna");
        INSTANCE.put("JMD", "Jamaican Dollar");
        INSTANCE.put("JOD", "Jordanian Dinar");
        INSTANCE.put("JPY", "Japanese Yen");
        INSTANCE.put("KES", "Kenyan Shilling");
        INSTANCE.put("KGS", "Kyrgystani Som");
        INSTANCE.put("KHR", "Cambodian Riel");
        INSTANCE.put("KMF", "Comorian Franc");
        INSTANCE.put("KPW", "North Korean Won");
        INSTANCE.put("KRW", "South Korean Won");
        INSTANCE.put("KWD", "Kuwaiti Dinar");
        INSTANCE.put("KYD", "Cayman Islands Dollar");
        INSTANCE.put("KZT", "Kazakhstani Tenge");
        INSTANCE.put("LAK", "Laotian Kip");
        INSTANCE.put("LBP", "Lebanese Pound");
        INSTANCE.put("LKR", "Sri Lankan Rupee");
        INSTANCE.put("LRD", "Liberian Dollar");
        INSTANCE.put("LSL", "Lesotho Loti");
        INSTANCE.put("LTL", "Lithuanian Litas");
        INSTANCE.put("LVL", "Latvian Lats");
        INSTANCE.put("LYD", "Libyan Dinar");
        INSTANCE.put("MAD", "Moroccan Dirham");
        INSTANCE.put("MDL", "Moldovan Leu");
        INSTANCE.put("MGA", "Malagasy Ariary");
        INSTANCE.put("MKD", "Macedonian Denar");
        INSTANCE.put("MMK", "Myanma Kyat");
        INSTANCE.put("MNT", "Mongolian Tugrik");
        INSTANCE.put("MOP", "Macanese Pataca");
        INSTANCE.put("MRO", "Mauritanian Ouguiya");
        INSTANCE.put("MUR", "Mauritian Rupee");
        INSTANCE.put("MVR", "Maldivian Rufiyaa");
        INSTANCE.put("MWK", "Malawian Kwacha");
        INSTANCE.put("MXN", "Mexican Peso");
        INSTANCE.put("MYR", "Malaysian Ringgit");
        INSTANCE.put("MZN", "Mozambican Metical");
        INSTANCE.put("NAD", "Namibian Dollar");
        INSTANCE.put("NGN", "Nigerian Naira");
        INSTANCE.put("NIO", "Nicaraguan Córdoba");
        INSTANCE.put("NOK", "Norwegian Krone");
        INSTANCE.put("NPR", "Nepalese Rupee");
        INSTANCE.put("NZD", "New Zealand Dollar");
        INSTANCE.put("OMR", "Omani Rial");
        INSTANCE.put("PAB", "Panamanian Balboa");
        INSTANCE.put("PEN", "Peruvian Sol");
        INSTANCE.put("PGK", "Papua New Guinean Kina");
        INSTANCE.put("PHP", "Philippine Peso");
        INSTANCE.put("PKR", "Pakistani Rupee");
        INSTANCE.put("PLN", "Polish Zloty");
        INSTANCE.put("PYG", "Paraguayan Guarani");
        INSTANCE.put("QAR", "Qatari Rial");
        INSTANCE.put("RON", "Romanian Leu");
        INSTANCE.put("RSD", "Serbian Dinar");
        INSTANCE.put("RUB", "Russian Ruble");
        INSTANCE.put("RWF", "Rwandan Franc");
        INSTANCE.put("SAR", "Saudi Riyal");
        INSTANCE.put("SBD", "Solomon Islands Dollar");
        INSTANCE.put("SCR", "Seychellois Rupee");
        INSTANCE.put("SDG", "Sudanese Pound");
        INSTANCE.put("SEK", "Swedish Krona");
        INSTANCE.put("SGD", "Singapore Dollar");
        INSTANCE.put("SHP", "Saint Helena Pound");
        INSTANCE.put("SLL", "Sierra Leonean Leone");
        INSTANCE.put("SOS", "Somali Shilling");
        INSTANCE.put("SRD", "Surinamese Dollar");
        INSTANCE.put("SSP", "South Sudanese Pound");
        INSTANCE.put("STD", "São Tomé and Príncipe Dobra (pre-2018)");
        INSTANCE.put("STN", "São Tomé and Príncipe Dobra");
        INSTANCE.put("SVC", "Salvadoran Colón");
        INSTANCE.put("SYP", "Syrian Pound");
        INSTANCE.put("SZL", "Swazi Lilangeni");
        INSTANCE.put("THB", "Thai Baht");
        INSTANCE.put("TJS", "Tajikistani Somoni");
        INSTANCE.put("TMT", "Turkmenistani Manat");
        INSTANCE.put("TND", "Tunisian Dinar");
        INSTANCE.put("TOP", "Tongan Pa'anga");
        INSTANCE.put("TRY", "Turkish Lira");
        INSTANCE.put("TTD", "Trinidad and Tobago Dollar");
        INSTANCE.put("TWD", "New Taiwan Dollar");
        INSTANCE.put("TZS", "Tanzanian Shilling");
        INSTANCE.put("UAH", "Ukrainian Hryvnia");
        INSTANCE.put("UGX", "Ugandan Shilling");
        INSTANCE.put("USD", "United States Dollar");
        INSTANCE.put("UYU", "Uruguayan Peso");
        INSTANCE.put("UZS", "Uzbekistan Som");
        INSTANCE.put("VEF", "Venezuelan Bolívar Fuerte (pre-2018)");
        INSTANCE.put("VES", "Venezuelan Bolívar Soberano");
        INSTANCE.put("VND", "Vietnamese Dong");
        INSTANCE.put("VUV", "Vanuatu Vatu");
        INSTANCE.put("WST", "Samoan Tala");
        INSTANCE.put("XAF", "CFA Franc BEAC");
        INSTANCE.put("XAG", "Silver Ounce");
        INSTANCE.put("XAU", "Gold Ounce");
        INSTANCE.put("XCD", "East Caribbean Dollar");
        INSTANCE.put("XDR", "Special Drawing Rights");
        INSTANCE.put("XOF", "CFA Franc BCEAO");
        INSTANCE.put("XPD", "Palladium Ounce");
        INSTANCE.put("XPF", "CFP Franc");
        INSTANCE.put("XPT", "Platinum Ounce");
        INSTANCE.put("YER", "Yemeni Rial");
        INSTANCE.put("ZAR", "South African Rand");
        INSTANCE.put("ZMW", "Zambian Kwacha");
        INSTANCE.put("ZWL", "Zimbabwean Dollar (pre-2009)");
    }
}