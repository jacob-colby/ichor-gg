---
type: smite-build
god: Artemis
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Wild
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.51
  slot_order:
  - name: Tyrfing
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.58
    - name: Toxic Blade
      pick_rate: 0.09
      win_rate: 0.65
  - name: Odysseus' Bow
    pick_rate: 0.24
    win_rate: 0.58
    alternates:
    - name: Toxic Blade
      pick_rate: 0.1
      win_rate: 0.5
    - name: Hastened Fatalis
      pick_rate: 0.08
      win_rate: 0.51
  - name: Hastened Fatalis
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: Dominance
      pick_rate: 0.14
      win_rate: 0.57
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.62
  - name: Dominance
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.58
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.62
  - name: Qin's Blade
    pick_rate: 0.11
    win_rate: 0.57
    alternates:
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.55
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.67
  - name: Bow
    pick_rate: 0.1
    win_rate: 0.4
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.47
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/artemis/
  last_verified: '2026-08-01'
  god_win_rate: 0.5831578947368421
  god_matches_won: 277
  god_matches_played: 475
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Damaru
  - The Crusher
  flex_slots:
  - The Crusher
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Damaru, Berserker''s Shield, The Crusher, Golden Blade,
    Hydra''s Lament, Runeforged Hammer, Jotunn''s Revenge, Riptalon, Demon Blade,
    Pharaoh''s Curse, Avenging Blade, Genji''s Guard, The Reaper, Tekko-Kagi, Eros''
    Bow, Oni Hunter''s Garb, Barbed Carver, Musashi''s Dual Swords, Shogun''s Ofuda,
    Yogi''s Necklace, Arondight, Breastplate of Valor, Kinetic Cuirass, Heartseeker,
    Bloodforge, Amanita Charm.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.5
    Lernaean Bow:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.6
    Damaru:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Musashi's Dual Swords
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Damaru, Berserker''s Shield, The Crusher, Hydra''s Lament,
    Golden Blade, Runeforged Hammer, Jotunn''s Revenge, Demon Blade, Riptalon, Pharaoh''s
    Curse, Genji''s Guard, Avenging Blade, The Reaper, Tekko-Kagi, Eros'' Bow, Musashi''s
    Dual Swords, Oni Hunter''s Garb, Yogi''s Necklace, Barbed Carver, Shogun''s Ofuda,
    Breastplate of Valor, Kinetic Cuirass, Arondight, Amanita Charm, Rage, Heartseeker.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.27
    Tyrfing:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.55
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.52
    Damaru:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tyrfing
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Runeforged
    Hammer, Riptalon, Kinetic Cuirass, Pharaoh''s Curse, Lernaean Bow, The Reaper,
    Golden Blade, Oni Hunter''s Garb, The Crusher, Eye of Providence, Chandra''s Grace,
    Hydra''s Lament, Genji''s Guard, Damaru, Avenging Blade, Jotunn''s Revenge, Spectral
    Armor, Bloodforge, Shogun''s Ofuda, Yogi''s Necklace, Phoenix Feather, Eye of
    the Storm, Shifter''s Shield, Shield Splitter, Eros'' Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Tyrfing:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.42
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Lernaean Bow
  - Avenging Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Tyrfing
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Riptalon, Avenging Blade, Lernaean
    Bow, The Reaper, Berserker''s Shield, Damaru, Hydra''s Lament, Runeforged Hammer,
    Tekko-Kagi, Golden Blade, Heartseeker, Avatar''s Parashu, Genji''s Guard, Pharaoh''s
    Curse, Titan''s Bane, Oni Hunter''s Garb, Demon Blade, Yogi''s Necklace, Kinetic
    Cuirass, Eros'' Bow, Breastplate of Valor, Pendulum Blade, Screeching Gargoyle,
    Amanita Charm, Oath-Sworn Spear.'
  slot_scores:
    Lernaean Bow:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Avenging Blade:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.46
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Hydra's Lament
  - Damaru
  - The Crusher
  flex_slots:
  - Golden Blade
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Lernaean Bow, Damaru, Berserker''s Shield, The Crusher,
    Golden Blade, Hydra''s Lament, Runeforged Hammer, Jotunn''s Revenge, Riptalon,
    Demon Blade, Pharaoh''s Curse, Avenging Blade, Genji''s Guard, The Reaper, Tekko-Kagi,
    Eros'' Bow, Oni Hunter''s Garb, Barbed Carver, Musashi''s Dual Swords, Shogun''s
    Ofuda, Yogi''s Necklace, Arondight, Breastplate of Valor, Kinetic Cuirass, Heartseeker,
    Bloodforge, Amanita Charm.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.5
    Lernaean Bow:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.29
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.35
    Damaru:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
---
