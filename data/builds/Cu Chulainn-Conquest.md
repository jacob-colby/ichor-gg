---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.33
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.44
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.27
      win_rate: 0.52
    - name: Mystical Mail
      pick_rate: 0.19
      win_rate: 0.54
  - name: Sanguine Lash
    pick_rate: 0.31
    win_rate: 0.49
    alternates:
    - name: Mystical Mail
      pick_rate: 0.15
      win_rate: 0.36
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.35
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.62
    - name: Umbral Link
      pick_rate: 0.11
      win_rate: 0.55
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.21
      win_rate: 0.49
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.57
  - name: Hide of the Nemean Lion
    pick_rate: 0.13
    win_rate: 0.23
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.65
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.6
  - name: Spectral Armor
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.38
    - name: Sage's Ring
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.41
  - name: Hunter's Cowl
    pick_rate: 0.09
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-10-09'
  god_win_rate: 0.5351351351351351
  god_matches_won: 99
  god_matches_played: 185
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade,
    Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s Guard, Eye
    of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament, Avenging
    Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer, Erosion,
    Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch Bow, Draconic
    Scale, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.44
    Spectral Armor:
      total: 0.51
      efficiency: 0.5
      win: 0.63
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Spectral Armor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Shield of the
    Phoenix, Runeforged Hammer, Golden Blade, Shield Splitter, Eye of the Storm, Genji''s
    Guard, Breastplate of Valor, The Reaper, Yogi''s Necklace, Pharaoh''s Curse, Lernaean
    Bow, Erosion, Shogun''s Ofuda, Phoenix Feather, Eye of Providence, Tyrfing, Avenging
    Blade, Riptalon, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Stone of Binding,
    Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.47
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.26
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.27
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.54
    Spectral Armor:
      total: 0.51
      efficiency: 0.5
      win: 0.63
      pick: 0.25
      fit: 0.3
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.74
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Spectral Armor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Berserker''s Shield, Avenging Blade, Amanita
    Charm, Heartseeker, Tekko-Kagi, Stone of Binding, Silverbranch Bow, Screeching
    Gargoyle, Runeforged Hammer, Void Shield, Titan''s Bane, Golden Blade, The Crusher,
    Toxic Blade, Void Stone, Genji''s Guard, Breastplate of Valor, Lernaean Bow, The
    Reaper, Shield Splitter, Tyrfing, Hydra''s Lament, Eye of the Storm, Riptalon,
    Pharaoh''s Curse, Avatar''s Parashu.'
  slot_scores:
    Avenging Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.35
    Spectral Armor:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.25
      fit: 0.18
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
  community_ordered:
  - Kinetic Cuirass
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Tyrfing
  - Spectral Armor
  flex_slots:
  - Golden Blade
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Tyrfing, Riptalon, Lernaean Bow, Runeforged Hammer, Silverbranch Bow, Genji''s
    Guard, Breastplate of Valor, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda, Shield
    Splitter, Tekko-Kagi, Hydra''s Lament, The Reaper, Eye of the Storm, Daybreak
    Gavel, Dominance, Avenging Blade, Erosion, Heartseeker, Shield of the Phoenix,
    Qin''s Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.18
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.35
    Tyrfing:
      total: 0.48
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.59
    Spectral Armor:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.25
      fit: 0.18
  community_ordered:
  - Kinetic Cuirass
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spectral Armor
  flex_slots:
  - Breastplate of Valor
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of
    the Phoenix, Screeching Gargoyle, Runeforged Hammer, Golden Blade, Arondight,
    Lernaean Bow, Pharaoh''s Curse, Shield Splitter, Eye of Erebus, Tyrfing, Daybreak
    Gavel, Gladiator''s Shield, Shogun''s Ofuda, Eye of the Storm, Prophetic Cloak,
    Chandra''s Grace, Erosion, Avenging Blade, Eye of Providence, Silverbranch Bow,
    Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.34
    Spectral Armor:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.25
      fit: 0.17
  community_ordered:
  - Kinetic Cuirass
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Golden Blade, Runeforged Hammer, Lernaean Bow, Shield Splitter, Tyrfing, Genji''s
    Guard, Eye of the Storm, Breastplate of Valor, Pharaoh''s Curse, Hydra''s Lament,
    Avenging Blade, Tekko-Kagi, Shogun''s Ofuda, Dominance, Heartseeker, Deathbringer,
    Erosion, Daybreak Gavel, Eye of Providence, Shield of the Phoenix, Silverbranch
    Bow, Draconic Scale, Toxic Blade, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.19
      fit: 0.44
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
