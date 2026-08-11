---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.44
  slot_order:
  - name: Tyrfing
    pick_rate: 0.47
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.25
      win_rate: 0.58
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.56
  - name: Toxic Blade
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.57
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.54
  - name: Silverbranch Bow
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.56
    - name: Dominance
      pick_rate: 0.16
      win_rate: 0.57
  - name: Riptalon
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.17
      win_rate: 0.6
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.53
  - name: Qin's Blade
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.63
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.6
  - name: Bow
    pick_rate: 0.09
    win_rate: 0.55
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.52
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.47
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.34
    win_rate: 0.6
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.63
  - name: Gilded Arrow
    pick_rate: 0.19
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-08-10'
  god_win_rate: 0.5410216718266254
  god_matches_won: 699
  god_matches_played: 1292
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Damaru
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
    this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, Lernaean Bow, Damaru,
    Golden Blade, Genji''s Guard, Hydra''s Lament, The Reaper, Tekko-Kagi, Pharaoh''s
    Curse, Breastplate of Valor, Demon Blade, Runeforged Hammer, Deathbringer, Heartseeker,
    Kinetic Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Eros'' Bow,
    Eye of Providence, Musashi''s Dual Swords, Freya''s Tears.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.52
    Damaru:
      total: 0.51
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Riptalon
  - Damaru
  - Demon Blade
  - The Crusher
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, Damaru, Lernaean
    Bow, Genji''s Guard, Golden Blade, Hydra''s Lament, The Reaper, Tekko-Kagi, Breastplate
    of Valor, Pharaoh''s Curse, Demon Blade, Runeforged Hammer, Deathbringer, Kinetic
    Cuirass, Amanita Charm, Shogun''s Ofuda, Heartseeker, Oni Hunter''s Garb, Musashi''s
    Dual Swords, Eye of Providence, Eros'' Bow, Freya''s Tears, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.5
    Damaru:
      total: 0.51
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.46
    Demon Blade:
      total: 0.48
      efficiency: 0.37
      win: 0.54
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Genji''s Guard, Berserker''s Shield, Hydra''s
    Lament, Breastplate of Valor, Lernaean Bow, Damaru, The Reaper, Golden Blade,
    Tekko-Kagi, Runeforged Hammer, Pharaoh''s Curse, Freya''s Tears, Kinetic Cuirass,
    Heartseeker, Amanita Charm, Oni Hunter''s Garb, Shield of the Phoenix, Eye of
    Providence, Pendulum Blade, Shogun''s Ofuda, Yogi''s Necklace, Titan''s Bane,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.54
      pick: 0.0
      fit: 0.13
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.43
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.54
      pick: 0.3
      fit: 0.37
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, The Crusher, Genji''s Guard, Jotunn''s Revenge, Pharaoh''s Curse,
    Oni Hunter''s Garb, Golden Blade, Chandra''s Grace, Breastplate of Valor, Lernaean
    Bow, Damaru, Runeforged Hammer, Shogun''s Ofuda, Phoenix Feather, Freya''s Tears,
    Hydra''s Lament, Spectral Armor, Umbral Link, Shifter''s Shield, Erosion, Eye
    of the Storm, Shield Splitter, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.54
      pick: 0.0
      fit: 0.13
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.64
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Toxic Blade
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, The Reaper,
    Tekko-Kagi, Lernaean Bow, Damaru, Genji''s Guard, Avenging Blade, Hydra''s Lament,
    Golden Blade, Heartseeker, Screeching Gargoyle, Breastplate of Valor, Pharaoh''s
    Curse, Runeforged Hammer, Stone of Binding, Titan''s Bane, Kinetic Cuirass, Void
    Shield, Amanita Charm, Oni Hunter''s Garb, Pendulum Blade, Eye of Providence.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.42
      win: 0.58
      pick: 0.3
      fit: 0.53
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.61
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.54
      win: 0.54
      pick: 0.3
      fit: 0.53
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, The Crusher, Jotunn''s Revenge, Golden Blade, Lernaean
    Bow, Damaru, Genji''s Guard, Hydra''s Lament, Pharaoh''s Curse, Breastplate of
    Valor, Tekko-Kagi, The Reaper, Runeforged Hammer, Kinetic Cuirass, Amanita Charm,
    Shogun''s Ofuda, Demon Blade, Oni Hunter''s Garb, Eye of Providence, Eros'' Bow,
    Heartseeker, Deathbringer, Freya''s Tears, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.54
      pick: 0.47
      fit: 0.64
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.62
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.54
      win: 0.54
      pick: 0.3
      fit: 0.54
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.54
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
  - Berserker's Shield
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
    Breastplate of Valor, Hydra''s Lament, Berserker''s Shield, The Crusher, Freya''s
    Tears, Lernaean Bow, Damaru, Shield of the Phoenix, Golden Blade, Screeching Gargoyle,
    Pharaoh''s Curse, Chandra''s Grace, Kinetic Cuirass, The Reaper, Amanita Charm,
    Arondight, Runeforged Hammer, Oni Hunter''s Garb, Eye of Providence, Pendulum
    Blade, Tekko-Kagi, Shogun''s Ofuda, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.54
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.18
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.54
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
  - Lernaean Bow
  - Damaru
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
    Underrated for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield,
    Lernaean Bow, Damaru, Golden Blade, Genji''s Guard, Hydra''s Lament, The Reaper,
    Tekko-Kagi, Pharaoh''s Curse, Breastplate of Valor, Demon Blade, Runeforged Hammer,
    Deathbringer, Heartseeker, Kinetic Cuirass, Shogun''s Ofuda, Amanita Charm, Oni
    Hunter''s Garb, Eros'' Bow, Eye of Providence, Musashi''s Dual Swords, Freya''s
    Tears.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.25
      fit: 0.52
    Damaru:
      total: 0.51
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.44
  starter: *id001
---
