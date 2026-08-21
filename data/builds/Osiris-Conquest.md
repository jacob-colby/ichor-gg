---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.51
    win_rate: 0.47
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 0.45
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.33
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.38
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.53
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.14
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.41
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.33
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.13
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.38
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.34
    win_rate: 0.51
  - name: Death's Toll
    pick_rate: 0.24
    win_rate: 0.42
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-21'
  god_win_rate: 0.44664031620553357
  god_matches_won: 113
  god_matches_played: 253
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Jotunn''s Revenge, Runeforged Hammer, Genji''s
    Guard, Pharaoh''s Curse, Damaru, Lernaean Bow, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of the Storm, Shogun''s Ofuda, Breastplate of Valor, Dominance, Shield of
    the Phoenix, Shield Splitter, Spectral Armor, Freya''s Tears, Avenging Blade,
    Tyrfing, Erosion, Eye of Providence, Leviathan''s Hide, Draconic Scale, Midgardian
    Mail, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.45
      pick: 0.17
      fit: 0.57
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.45
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.46
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Shield of the Phoenix
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, The Crusher, Yogi''s Necklace,
    Genji''s Guard, Riptalon, Pharaoh''s Curse, Jotunn''s Revenge, The Reaper, Runeforged
    Hammer, Chandra''s Grace, Oni Hunter''s Garb, Phoenix Feather, Eye of the Storm,
    Freya''s Tears, Spectral Armor, Shield Splitter, Damaru, Shogun''s Ofuda, Breastplate
    of Valor, Erosion, Lernaean Bow, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.45
      pick: 0.17
      fit: 0.53
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.47
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.48
      efficiency: 0.52
      win: 0.47
      pick: 0.51
      fit: 0.44
    The Crusher:
      total: 0.48
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.46
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Amanita Charm, Genji''s
    Guard, Riptalon, The Reaper, Runeforged Hammer, Void Shield, Silverbranch Bow,
    Stone of Binding, Screeching Gargoyle, Tekko-Kagi, Oni Hunter''s Garb, Heartseeker,
    Pharaoh''s Curse, Damaru, Void Stone, Titan''s Bane, Hydra''s Lament, Breastplate
    of Valor, Lernaean Bow, Toxic Blade, Spectral Armor, Freya''s Tears, Shield of
    the Phoenix, Eye of the Storm.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.48
      win: 0.46
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.46
      efficiency: 0.69
      win: 0.46
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.33
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.47
      efficiency: 0.63
      win: 0.46
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Riptalon, Genji''s Guard, Pharaoh''s Curse,
    Jotunn''s Revenge, Tyrfing, Oni Hunter''s Garb, Runeforged Hammer, Silverbranch
    Bow, Lernaean Bow, Shogun''s Ofuda, Breastplate of Valor, Damaru, Hydra''s Lament,
    Spectral Armor, Freya''s Tears, Dominance, Shield of the Phoenix, Toxic Blade,
    Eye of the Storm, Erosion, Leviathan''s Hide, Shield Splitter, Eye of Providence,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.53
      win: 0.45
      pick: 0.17
      fit: 0.6
    Genji's Guard:
      total: 0.46
      efficiency: 0.69
      win: 0.46
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.51
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.41
    Riptalon:
      total: 0.46
      efficiency: 0.53
      win: 0.46
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.47
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.25
    Amanita Charm:
      total: 0.47
      efficiency: 0.63
      win: 0.46
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Breastplate of Valor, Freya''s Tears, Shield of the Phoenix, Hydra''s Lament,
    Amanita Charm, The Crusher, Gladiator''s Shield, Chandra''s Grace, Oni Hunter''s
    Garb, Pharaoh''s Curse, Screeching Gargoyle, Runeforged Hammer, Spectral Armor,
    Damaru, Shogun''s Ofuda, Lernaean Bow, Arondight, Erosion, Leviathan''s Hide,
    Eye of the Storm, Eye of Providence, Yogi''s Necklace, Midgardian Mail, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.46
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.33
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.4
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.48
      efficiency: 0.59
      win: 0.46
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
    Garb, Hydra''s Lament, Eye of the Storm, Shogun''s Ofuda, Breastplate of Valor,
    Dominance, Shield of the Phoenix, Shield Splitter, Spectral Armor, Freya''s Tears,
    Avenging Blade, Tyrfing, Erosion, Eye of Providence, Leviathan''s Hide, Draconic
    Scale, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.53
      win: 0.45
      pick: 0.17
      fit: 0.57
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.46
      pick: 0.3
      fit: 0.45
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.59
      win: 0.38
      pick: 0.2
      fit: 0.45
    The Crusher:
      total: 0.49
      efficiency: 0.64
      win: 0.46
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.46
      pick: 0.0
      fit: 0.35
  starter: *id001
---
