---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.33
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.61
    win_rate: 0.43
    alternates:
    - name: Golden Blade
      pick_rate: 0.13
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.04
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.17
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.33
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.4
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.33
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.17
    win_rate: 0.25
    alternates:
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.0
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.16
      win_rate: 0.33
    - name: Medallion
      pick_rate: 0.11
      win_rate: 0.5
  - name: Veve Charm
    pick_rate: 0.14
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 1.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.14
      win_rate: 0.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.39
    win_rate: 0.44
  - name: Death's Toll
    pick_rate: 0.26
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-13'
  god_win_rate: 0.34782608695652173
  god_matches_won: 8
  god_matches_played: 23
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Pharaoh''s
    Curse, Lernaean Bow, Runeforged Hammer, Damaru, Oni Hunter''s Garb, Hydra''s Lament,
    Breastplate of Valor, Eye of the Storm, Shield Splitter, Shield of the Phoenix,
    Spectral Armor, Freya''s Tears, Dominance, Tyrfing, Erosion, Riptalon, Yogi''s
    Necklace, Eye of Providence, Eros'' Bow, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.57
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.13
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.45
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.66
      win: 0.42
      pick: 0.0
      fit: 0.3
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.35
      fit: 0.35
    The Crusher:
      total: 0.46
      efficiency: 0.63
      win: 0.42
      pick: 0.0
      fit: 0.37
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Riptalon, Pharaoh''s
    Curse, The Crusher, Jotunn''s Revenge, Oni Hunter''s Garb, Runeforged Hammer,
    The Reaper, Chandra''s Grace, Lernaean Bow, Breastplate of Valor, Damaru, Freya''s
    Tears, Phoenix Feather, Hydra''s Lament, Eye of the Storm, Shield Splitter, Spectral
    Armor, Erosion, Eye of Providence, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.53
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.16
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.47
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.57
      win: 0.42
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.35
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.42
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Riptalon, Amanita
    Charm, Silverbranch Bow, Stone of Binding, Pharaoh''s Curse, Void Shield, Lernaean
    Bow, Runeforged Hammer, The Reaper, Oni Hunter''s Garb, Screeching Gargoyle, Breastplate
    of Valor, Hydra''s Lament, Tekko-Kagi, Damaru, Void Stone, Heartseeker, Freya''s
    Tears, Spectral Armor, Shield of the Phoenix, Toxic Blade, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.42
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.1
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.33
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.66
      win: 0.42
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.35
      fit: 0.26
    The Crusher:
      total: 0.49
      efficiency: 0.63
      win: 0.42
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  - Riptalon
  flex_slots:
  - Riptalon
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Kinetic Cuirass, Pharaoh''s Curse, Amanita Charm, The Crusher,
    Jotunn''s Revenge, Lernaean Bow, Silverbranch Bow, Tyrfing, Oni Hunter''s Garb,
    Breastplate of Valor, Runeforged Hammer, Hydra''s Lament, Damaru, Freya''s Tears,
    Spectral Armor, Shield of the Phoenix, Eros'' Bow, Dominance, Yogi''s Necklace,
    Toxic Blade, Eye of the Storm, Erosion, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.6
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.1
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.41
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.59
      win: 0.42
      pick: 0.0
      fit: 0.36
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.35
      fit: 0.26
    Riptalon:
      total: 0.45
      efficiency: 0.56
      win: 0.42
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Draconic Scale
  flex_slots:
  - Golden Blade
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Gladiator''s Shield, Hydra''s Lament, Freya''s Tears, Shield of the Phoenix,
    Kinetic Cuirass, Amanita Charm, The Crusher, Pharaoh''s Curse, Oni Hunter''s Garb,
    Chandra''s Grace, Screeching Gargoyle, Lernaean Bow, Runeforged Hammer, Damaru,
    Spectral Armor, Yogi''s Necklace, Riptalon, Arondight, Erosion, Leviathan''s Hide,
    Eye of the Storm, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.34
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.3
      fit: 0.36
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.33
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.66
      win: 0.42
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.66
      win: 0.42
      pick: 0.0
      fit: 0.4
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.35
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Amanita Charm
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita
    Charm, Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer, Damaru, Oni Hunter''s
    Garb, Hydra''s Lament, Breastplate of Valor, Eye of the Storm, Shield Splitter,
    Shield of the Phoenix, Spectral Armor, Freya''s Tears, Dominance, Avenging Blade,
    Tyrfing, Erosion, Riptalon, Yogi''s Necklace, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.15
      fit: 0.57
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.4
      pick: 0.34
      fit: 0.45
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.66
      win: 0.42
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.59
      win: 0.42
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.46
      efficiency: 0.63
      win: 0.42
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.46
      efficiency: 0.63
      win: 0.42
      pick: 0.0
      fit: 0.35
  starter: *id001
---
