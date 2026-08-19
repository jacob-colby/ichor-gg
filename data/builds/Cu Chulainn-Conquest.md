---
type: smite-build
god: Cu Chulainn
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Warped
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.43
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.48
    alternates:
    - name: Mystical Mail
      pick_rate: 0.18
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.04
      win_rate: 0.63
  - name: Mystical Mail
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.12
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.47
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.56
  - name: Kinetic Cuirass
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.49
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.51
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.48
    alternates:
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.4
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.59
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.62
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.5
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.37
  - name: Bumba's Cudgel
    pick_rate: 0.06
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/cu-chulainn/
  last_verified: '2026-08-19'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
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
    this god: Berserker''s Shield, The Crusher, Amanita Charm, Golden Blade, Jotunn''s
    Revenge, Runeforged Hammer, Pharaoh''s Curse, Damaru, Lernaean Bow, Freya''s Tears,
    Oni Hunter''s Garb, Hydra''s Lament, Eye of the Storm, Breastplate of Valor, Shogun''s
    Ofuda, Shield Splitter, Shield of the Phoenix, Tyrfing, Spectral Armor, Avenging
    Blade, Erosion, Eye of Providence, Dominance, Leviathan''s Hide, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.44
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.34
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.49
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.34
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - The Crusher
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, The Crusher,
    Golden Blade, Riptalon, Pharaoh''s Curse, Jotunn''s Revenge, The Reaper, Freya''s
    Tears, Runeforged Hammer, Chandra''s Grace, Oni Hunter''s Garb, Phoenix Feather,
    Eye of the Storm, Spectral Armor, Shield Splitter, Damaru, Shogun''s Ofuda, Breastplate
    of Valor, Erosion, Lernaean Bow, Eye of Providence, Hydra''s Lament, Avenging
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.54
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.63
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.44
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, Avenging Blade,
    Amanita Charm, Riptalon, The Reaper, Silverbranch Bow, Golden Blade, Runeforged
    Hammer, Stone of Binding, Void Shield, Screeching Gargoyle, Tekko-Kagi, Freya''s
    Tears, Damaru, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s Lament, Void Stone,
    Lernaean Bow, Breastplate of Valor, Toxic Blade, Spectral Armor, Heartseeker,
    Shield of the Phoenix, Eye of the Storm.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.48
      win: 0.48
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.35
    Draconic Scale:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.25
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Draconic Scale
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, The Crusher, Riptalon, Amanita Charm,
    Pharaoh''s Curse, Jotunn''s Revenge, Tyrfing, Silverbranch Bow, Freya''s Tears,
    Lernaean Bow, Oni Hunter''s Garb, Runeforged Hammer, Breastplate of Valor, Shogun''s
    Ofuda, Damaru, Hydra''s Lament, Spectral Armor, Shield of the Phoenix, Toxic Blade,
    Eye of the Storm, Erosion, Shield Splitter, Leviathan''s Hide, The Reaper, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.35
    Draconic Scale:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.25
    Riptalon:
      total: 0.47
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.48
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Berserker''s Shield, Breastplate of Valor, Shield of the Phoenix, Hydra''s Lament,
    The Crusher, Amanita Charm, Chandra''s Grace, Screeching Gargoyle, Oni Hunter''s
    Garb, Pharaoh''s Curse, Runeforged Hammer, Golden Blade, Damaru, Spectral Armor,
    Lernaean Bow, Shogun''s Ofuda, Arondight, Erosion, Leviathan''s Hide, Eye of Providence,
    Eye of the Storm, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.47
      pick: 0.19
      fit: 0.36
    Berserker's Shield:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.34
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.49
      pick: 0.13
      fit: 0.43
    Draconic Scale:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.24
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
    Underrated for this god: Berserker''s Shield, The Crusher, Amanita Charm, Golden
    Blade, Jotunn''s Revenge, Runeforged Hammer, Pharaoh''s Curse, Damaru, Lernaean
    Bow, Oni Hunter''s Garb, Hydra''s Lament, Eye of the Storm, Breastplate of Valor,
    Shogun''s Ofuda, Shield Splitter, Freya''s Tears, Shield of the Phoenix, Tyrfing,
    Spectral Armor, Avenging Blade, Erosion, Eye of Providence, Dominance, Leviathan''s
    Hide, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.59
      pick: 0.15
      fit: 0.44
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.48
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.49
      efficiency: 0.63
      win: 0.48
      pick: 0.0
      fit: 0.34
  starter: *id001
---
