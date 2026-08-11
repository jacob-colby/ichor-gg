---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.55
  slot_order:
  - name: Tyrfing
    pick_rate: 0.47
    win_rate: 0.55
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.25
      win_rate: 0.58
    - name: Dominance
      pick_rate: 0.08
      win_rate: 0.55
  - name: Toxic Blade
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.57
    - name: Dagger of Frenzy
      pick_rate: 0.13
      win_rate: 0.6
  - name: Silverbranch Bow
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.57
    - name: Dominance
      pick_rate: 0.15
      win_rate: 0.56
  - name: Riptalon
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.17
      win_rate: 0.6
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.52
  - name: Qin's Blade
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.63
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.56
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.51
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.44
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.33
    win_rate: 0.59
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.63
  - name: Gilded Arrow
    pick_rate: 0.19
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-08-11'
  god_win_rate: 0.5418181818181819
  god_matches_won: 745
  god_matches_played: 1375
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Crusher, Dominance, Berserker''s Shield, Jotunn''s Revenge,
    Lernaean Bow, Damaru, Golden Blade, Hydra''s Lament, Genji''s Guard, The Reaper,
    Runeforged Hammer, Tekko-Kagi, Demon Blade, Pharaoh''s Curse, Breastplate of Valor,
    Amanita Charm, Oni Hunter''s Garb, Heartseeker, Yogi''s Necklace, Kinetic Cuirass,
    Shogun''s Ofuda, Avenging Blade, Musashi''s Dual Swords, Eros'' Bow, Eye of Providence,
    Shield Splitter.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.54
    Dominance:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.15
      fit: 0.44
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.52
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Musashi's Dual Swords
  - Riptalon
  - Damaru
  - Demon Blade
  - The Crusher
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Crusher, Berserker''s Shield, Jotunn''s Revenge, Dominance,
    Damaru, Lernaean Bow, Hydra''s Lament, Genji''s Guard, Golden Blade, The Reaper,
    Runeforged Hammer, Tekko-Kagi, Demon Blade, Pharaoh''s Curse, Breastplate of Valor,
    Amanita Charm, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Heartseeker,
    Musashi''s Dual Swords, Shogun''s Ofuda, Avenging Blade, Eye of Providence, Eros''
    Bow, Rage.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.5
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.5
    Damaru:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - The Crusher
  flex_slots:
  - Tyrfing
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Riptalon, Berserker''s Shield, Genji''s Guard,
    Hydra''s Lament, Dominance, Lernaean Bow, Damaru, Breastplate of Valor, The Reaper,
    Runeforged Hammer, Golden Blade, Tekko-Kagi, Amanita Charm, Oni Hunter''s Garb,
    Pharaoh''s Curse, Yogi''s Necklace, Kinetic Cuirass, Heartseeker, Freya''s Tears,
    Shield of the Phoenix, Eye of Providence, Pendulum Blade, Arondight, Avenging
    Blade, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.13
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.4
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.43
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Riptalon, Berserker''s Shield, Shield of the Phoenix,
    Kinetic Cuirass, The Reaper, The Crusher, Genji''s Guard, Eye of Providence, Jotunn''s
    Revenge, Oni Hunter''s Garb, Pharaoh''s Curse, Runeforged Hammer, Golden Blade,
    Chandra''s Grace, Lernaean Bow, Damaru, Hydra''s Lament, Breastplate of Valor,
    Yogi''s Necklace, Shogun''s Ofuda, Shifter''s Shield, Phoenix Feather, Spectral
    Armor, Freya''s Tears, Shield Splitter, Eye of the Storm, Erosion, Umbral Link.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.39
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.64
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Toxic Blade
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
    for this god: The Crusher, Riptalon, Jotunn''s Revenge, Berserker''s Shield, Dominance,
    The Reaper, Lernaean Bow, Tekko-Kagi, Avenging Blade, Damaru, Genji''s Guard,
    Hydra''s Lament, Golden Blade, Runeforged Hammer, Heartseeker, Screeching Gargoyle,
    Pharaoh''s Curse, Breastplate of Valor, Titan''s Bane, Amanita Charm, Oni Hunter''s
    Garb, Stone of Binding, Yogi''s Necklace, Kinetic Cuirass, Pendulum Blade, Void
    Shield.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.42
      win: 0.59
      pick: 0.22
      fit: 0.53
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.51
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.46
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.61
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.18
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Toxic Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Berserker''s Shield, The Crusher, Dominance, Golden Blade,
    Jotunn''s Revenge, Lernaean Bow, Damaru, Genji''s Guard, Hydra''s Lament, Runeforged
    Hammer, Pharaoh''s Curse, The Reaper, Tekko-Kagi, Breastplate of Valor, Amanita
    Charm, Oni Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Demon Blade, Shogun''s
    Ofuda, Eye of Providence, Eros'' Bow, Heartseeker, Avenging Blade, Freya''s Tears.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.42
      win: 0.59
      pick: 0.22
      fit: 0.54
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Tyrfing:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.47
      fit: 0.64
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.62
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.53
      pick: 0.18
      fit: 0.54
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Hydra''s Lament, Berserker''s Shield, Breastplate of Valor, The Crusher, Riptalon,
    Dominance, Lernaean Bow, Damaru, Freya''s Tears, Shield of the Phoenix, Runeforged
    Hammer, Golden Blade, Amanita Charm, Arondight, Pharaoh''s Curse, Oni Hunter''s
    Garb, Screeching Gargoyle, Chandra''s Grace, The Reaper, Yogi''s Necklace, Kinetic
    Cuirass, Pendulum Blade, Tekko-Kagi, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Damaru
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Berserker''s Shield, Jotunn''s Revenge,
    Lernaean Bow, Damaru, Riptalon, Golden Blade, Hydra''s Lament, Genji''s Guard,
    The Reaper, Dominance, Runeforged Hammer, Tekko-Kagi, Demon Blade, Pharaoh''s
    Curse, Breastplate of Valor, Amanita Charm, Oni Hunter''s Garb, Heartseeker, Yogi''s
    Necklace, Kinetic Cuirass, Shogun''s Ofuda, Avenging Blade, Musashi''s Dual Swords,
    Eros'' Bow, Eye of Providence, Shield Splitter.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.15
      fit: 0.52
    Damaru:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
---
