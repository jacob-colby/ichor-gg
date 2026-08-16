---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.47
    win_rate: 0.44
    alternates:
    - name: Golden Blade
      pick_rate: 0.18
      win_rate: 0.43
    - name: Berserker's Shield
      pick_rate: 0.04
      win_rate: 0.2
  - name: Berserker's Shield
    pick_rate: 0.23
    win_rate: 0.46
    alternates:
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.43
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.45
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.27
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.18
      win_rate: 0.48
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.42
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.29
    - name: Shogun's Ofuda
      pick_rate: 0.09
      win_rate: 0.4
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.45
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.4
  - name: Contagion
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.39
    win_rate: 0.45
  - name: Death's Toll
    pick_rate: 0.25
    win_rate: 0.39
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-16'
  god_win_rate: 0.4298245614035088
  god_matches_won: 49
  god_matches_played: 114
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Jotunn''s Revenge, Runeforged Hammer, Genji''s
    Guard, Pharaoh''s Curse, Damaru, Lernaean Bow, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of the Storm, Breastplate of Valor, Shield of the Phoenix, Shield Splitter,
    Spectral Armor, Freya''s Tears, Avenging Blade, Tyrfing, Erosion, Eye of Providence,
    Leviathan''s Hide, Dominance, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.49
      efficiency: 0.39
      win: 0.67
      pick: 0.28
      fit: 0.26
    Golden Blade:
      total: 0.47
      efficiency: 0.53
      win: 0.43
      pick: 0.18
      fit: 0.57
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.45
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.3
    The Crusher:
      total: 0.47
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Shield of the Phoenix
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Crusher, Genji''s Guard, Riptalon,
    Pharaoh''s Curse, Jotunn''s Revenge, The Reaper, Runeforged Hammer, Chandra''s
    Grace, Oni Hunter''s Garb, Phoenix Feather, Eye of the Storm, Freya''s Tears,
    Spectral Armor, Shield Splitter, Damaru, Breastplate of Valor, Erosion, Lernaean
    Bow, Eye of Providence, Hydra''s Lament, Avenging Blade.'
  slot_scores:
    Contagion:
      total: 0.49
      efficiency: 0.39
      win: 0.67
      pick: 0.28
      fit: 0.27
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.47
    Shield of the Phoenix:
      total: 0.49
      efficiency: 0.57
      win: 0.43
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.47
      efficiency: 0.52
      win: 0.44
      pick: 0.47
      fit: 0.44
    The Crusher:
      total: 0.47
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Amanita Charm, Genji''s
    Guard, Riptalon, The Reaper, Runeforged Hammer, Void Shield, Silverbranch Bow,
    Stone of Binding, Screeching Gargoyle, Tekko-Kagi, Oni Hunter''s Garb, Pharaoh''s
    Curse, Damaru, Void Stone, Hydra''s Lament, Breastplate of Valor, Lernaean Bow,
    Toxic Blade, Spectral Armor, Freya''s Tears, Shield of the Phoenix, Eye of the
    Storm, Heartseeker.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.39
      win: 0.67
      pick: 0.28
      fit: 0.22
    Avenging Blade:
      total: 0.46
      efficiency: 0.48
      win: 0.43
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.33
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.45
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Riptalon, Genji''s Guard, Pharaoh''s Curse,
    Jotunn''s Revenge, Tyrfing, Oni Hunter''s Garb, Runeforged Hammer, Silverbranch
    Bow, Lernaean Bow, Breastplate of Valor, Damaru, Hydra''s Lament, Spectral Armor,
    Freya''s Tears, Shield of the Phoenix, Toxic Blade, Eye of the Storm, Erosion,
    Leviathan''s Hide, Shield Splitter, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.39
      win: 0.67
      pick: 0.28
      fit: 0.22
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.43
      pick: 0.18
      fit: 0.6
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.41
    Riptalon:
      total: 0.45
      efficiency: 0.53
      win: 0.43
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.46
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.25
    Amanita Charm:
      total: 0.45
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Breastplate of Valor, Freya''s Tears, Shield of the Phoenix, Hydra''s Lament,
    Amanita Charm, The Crusher, Chandra''s Grace, Oni Hunter''s Garb, Pharaoh''s Curse,
    Screeching Gargoyle, Runeforged Hammer, Spectral Armor, Gladiator''s Shield, Damaru,
    Lernaean Bow, Arondight, Erosion, Leviathan''s Hide, Eye of the Storm, Eye of
    Providence, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.48
      efficiency: 0.39
      win: 0.67
      pick: 0.28
      fit: 0.21
    Genji's Guard:
      total: 0.49
      efficiency: 0.69
      win: 0.43
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.33
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.4
    Freya's Tears:
      total: 0.46
      efficiency: 0.59
      win: 0.43
      pick: 0.0
      fit: 0.43
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Amanita Charm, Jotunn''s Revenge, Runeforged
    Hammer, Genji''s Guard, Pharaoh''s Curse, Damaru, Lernaean Bow, Oni Hunter''s
    Garb, Hydra''s Lament, Eye of the Storm, Breastplate of Valor, Shield of the Phoenix,
    Shield Splitter, Spectral Armor, Freya''s Tears, Avenging Blade, Tyrfing, Erosion,
    Eye of Providence, Leviathan''s Hide, Dominance, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.53
      win: 0.43
      pick: 0.18
      fit: 0.57
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.31
      fit: 0.45
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.41
      efficiency: 0.59
      win: 0.27
      pick: 0.2
      fit: 0.45
    The Crusher:
      total: 0.47
      efficiency: 0.64
      win: 0.43
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.63
      win: 0.43
      pick: 0.0
      fit: 0.35
  starter: *id001
---
