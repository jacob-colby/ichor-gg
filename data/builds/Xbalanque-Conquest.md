---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.57
  slot_order:
  - name: Tyrfing
    pick_rate: 0.48
    win_rate: 0.63
    alternates:
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.64
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.38
    win_rate: 0.6
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.66
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.61
  - name: Dominance
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.21
      win_rate: 0.7
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.49
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.62
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.61
  - name: Qin's Blade
    pick_rate: 0.1
    win_rate: 0.81
    alternates:
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.54
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.61
  - name: Riptalon
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Manchu Bow
      pick_rate: 0.12
      win_rate: 0.71
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.46
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-01'
  god_win_rate: 0.6
  god_matches_won: 201
  god_matches_played: 335
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
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Damaru
  flex_slots:
  - Damaru
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Lernaean Bow, Damaru, Berserker''s Shield, Blink Rune, Golden
    Blade, The Crusher, Runeforged Hammer, Demon Blade, Hydra''s Lament, Jotunn''s
    Revenge, Pharaoh''s Curse, Avenging Blade, Eros'' Bow, Tekko-Kagi, Genji''s Guard,
    The Reaper, Musashi''s Dual Swords, Shogun''s Ofuda, Barbed Carver, Oni Hunter''s
    Garb, Yogi''s Necklace, Bloodforge, Kinetic Cuirass, Rage, Amanita Charm, Arondight,
    Breastplate of Valor.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.58
      efficiency: 0.52
      win: 0.63
      pick: 0.48
      fit: 0.64
    Qin's Blade:
      total: 0.58
      efficiency: 0.41
      win: 0.81
      pick: 0.1
      fit: 0.43
    Riptalon:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.13
      fit: 0.46
    Damaru:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Qin's Blade
  - Musashi's Dual Swords
  - Riptalon
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Damaru, Lernaean Bow, Blink Rune, Berserker''s Shield, Golden
    Blade, Demon Blade, The Crusher, Runeforged Hammer, Hydra''s Lament, Jotunn''s
    Revenge, Pharaoh''s Curse, Avenging Blade, Genji''s Guard, Musashi''s Dual Swords,
    The Reaper, Eros'' Bow, Tekko-Kagi, Barbed Carver, Oni Hunter''s Garb, Shogun''s
    Ofuda, Rage, Yogi''s Necklace, Bloodforge, Kinetic Cuirass, Amanita Charm, Arondight,
    Deathbringer.'
  slot_scores:
    Tyrfing:
      total: 0.58
      efficiency: 0.52
      win: 0.63
      pick: 0.48
      fit: 0.6
    Qin's Blade:
      total: 0.57
      efficiency: 0.41
      win: 0.81
      pick: 0.1
      fit: 0.4
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.13
      fit: 0.42
    Damaru:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blink Rune
  - Berserker's Shield
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Blink Rune
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Amanita Charm, Berserker''s Shield, Blink Rune, Shield of
    the Phoenix, Runeforged Hammer, Kinetic Cuirass, Pharaoh''s Curse, Golden Blade,
    Lernaean Bow, Oni Hunter''s Garb, Eye of Providence, The Reaper, Chandra''s Grace,
    Damaru, The Crusher, Genji''s Guard, Avenging Blade, Hydra''s Lament, Spectral
    Armor, Shogun''s Ofuda, Bloodforge, Yogi''s Necklace, Phoenix Feather, Eye of
    the Storm, Shifter''s Shield, Jotunn''s Revenge, Eros'' Bow, Shield Splitter.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.48
      fit: 0.42
    Qin's Blade:
      total: 0.56
      efficiency: 0.41
      win: 0.81
      pick: 0.1
      fit: 0.3
    Riptalon:
      total: 0.61
      efficiency: 0.6
      win: 0.67
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Blink Rune
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
    for this god: Riptalon, The Crusher, Jotunn''s Revenge, Blink Rune, Avenging Blade,
    Lernaean Bow, The Reaper, Berserker''s Shield, Damaru, Tekko-Kagi, Runeforged
    Hammer, Hydra''s Lament, Golden Blade, Heartseeker, Avatar''s Parashu, Genji''s
    Guard, Pharaoh''s Curse, Titan''s Bane, Oni Hunter''s Garb, Demon Blade, Yogi''s
    Necklace, Eros'' Bow, Kinetic Cuirass, Amanita Charm, Pendulum Blade, Breastplate
    of Valor, Shogun''s Ofuda, Screeching Gargoyle.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.56
      efficiency: 0.52
      win: 0.63
      pick: 0.48
      fit: 0.46
    Qin's Blade:
      total: 0.56
      efficiency: 0.41
      win: 0.81
      pick: 0.1
      fit: 0.32
    Riptalon:
      total: 0.62
      efficiency: 0.6
      win: 0.67
      pick: 0.13
      fit: 0.64
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Blink Rune
  - Lernaean Bow
  - Berserker's Shield
  - Damaru
  - The Crusher
  flex_slots:
  - Golden Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Lernaean Bow, Damaru, Berserker''s Shield, Blink Rune,
    Golden Blade, The Crusher, Runeforged Hammer, Demon Blade, Hydra''s Lament, Riptalon,
    Jotunn''s Revenge, Pharaoh''s Curse, Avenging Blade, Eros'' Bow, Tekko-Kagi, Genji''s
    Guard, The Reaper, Musashi''s Dual Swords, Shogun''s Ofuda, Barbed Carver, Oni
    Hunter''s Garb, Yogi''s Necklace, Bloodforge, Kinetic Cuirass, Rage, Amanita Charm,
    Arondight, Breastplate of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Damaru:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Blink Rune
  - Lernaean Bow
  - Berserker's Shield
  - Qin's Blade
  - Damaru
  flex_slots:
  - Golden Blade
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Lernaean Bow, Damaru, Berserker''s
    Shield, Blink Rune, Golden Blade, The Crusher, Runeforged Hammer, Demon Blade,
    Hydra''s Lament, Riptalon, Jotunn''s Revenge, Pharaoh''s Curse, Avenging Blade,
    Eros'' Bow, Tekko-Kagi, Genji''s Guard, The Reaper, Musashi''s Dual Swords, Shogun''s
    Ofuda, Barbed Carver, Oni Hunter''s Garb, Yogi''s Necklace, Bloodforge, Kinetic
    Cuirass, Rage, Amanita Charm, Arondight, Breastplate of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.54
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Qin's Blade:
      total: 0.58
      efficiency: 0.41
      win: 0.81
      pick: 0.1
      fit: 0.43
    Damaru:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
  swaps:
  - added: Qin's Blade
    removed: The Crusher
    reason: community 81% win over 34 matches (vs 60% on this god), taking the model's
      weakest slot from The Crusher
  starter: *id001
---
