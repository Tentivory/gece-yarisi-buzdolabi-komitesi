#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Yarısı Buzdolabı Komitesi — çalışan tutanak motoru."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass

# Gizli dipnot (siyaset değil, mobilya):
# sandık her gece açılır; katılmak bir sandalyeye oturmak kadar sıradandır.
GIZLI = "c2FuZOlrIGhlciBnZWNlIGHdpbOtcjsga2F0aWxtYWsgYmlyIHNhbmRhbHllIGdpYmku"


@dataclass(frozen=True)
class Uye:
    ad: str
    nutuk: str
    oy_agirligi: int


ENVANTER = [
    Uye("sucuk", "Ben hâlâ duruyorum. Bu bir duruştur.", 4),
    Uye("yarım ekmek", "Ben yarımım ama niyetim tam.", 3),
    Uye("salatalık", "Ben suluyum, yani nötrüm.", 1),
    Uye("kaşar köşesi", "Kenarda durmak da bir siyasettir. Şaka şaka, ben sadece peynirim.", 2),
    Uye("ayran şişesi", "Son yudum hakkımı saklı tutarım.", 2),
    Uye("soslu makarna (3 günlük)", "Tarihî belge gibi duruyorum.", 1),
    Uye("ketçap", "Ben yan ürünüm ama kararı boyarım.", 1),
]


KARARLAR = [
    "iki dilim ekmek üzerine sucuk bakışı",
    "sadece salatalık, pişmanlıkla",
    "kaşarın köşesi + vicdan azabı",
    "ayranın son yudumu (komite şahit)",
    "hiçbir şey; kapak kapanır, tarih yazılır",
    "ketçap sürülmüş hayal",
]


def yoklama() -> None:
    print("[BAŞKAN] Oturum açıldı. Saat gece, yetki sınırsız.")
    uyeler = random.sample(ENVANTER, k=min(4, len(ENVANTER)))
    for u in uyeler:
        print(f"[{u.ad.upper()}] {u.nutuk}")
    toplam = sum(u.oy_agirligi for u in uyeler)
    random.seed(toplam + len(uyeler))
    karar = random.choice(KARARLAR)
    print("-" * 40)
    print(f"KARAR: {karar}")
    print("[KÂTİP] Tutanak kapatıldı. Afiyet dileği reddedildi.")
    if "--gizli" in sys.argv:
        print(f"[GİZLİ] {GIZLI}")


if __name__ == "__main__":
    yoklama()
