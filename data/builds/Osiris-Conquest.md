---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.58
    win_rate: 0.49
    alternates:
    - name: Golden Blade
      pick_rate: 0.14
      win_rate: 0.6
    - name: Berserker's Shield
      pick_rate: 0.05
      win_rate: 0.42
  - name: Berserker's Shield
    pick_rate: 0.32
    win_rate: 0.5
    alternates:
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.49
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.59
  - name: Kinetic Cuirass
    pick_rate: 0.19
    win_rate: 0.49
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.2
      win_rate: 0.46
    - name: Shogun's Ofuda
      pick_rate: 0.09
      win_rate: 0.47
  - name: Dwarven Plate
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.38
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.64
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.44
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.47
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.43
    win_rate: 0.58
  - name: Death's Toll
    pick_rate: 0.27
    win_rate: 0.38
  - name: Sundering Axe
    pick_rate: 0.1
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-11'
  god_win_rate: 0.49390243902439024
  god_matches_won: 243
  god_matches_played: 492
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
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
  - Hide of the Nemean Lion
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Pharaoh''s
    Curse, Lernaean Bow, Runeforged Hammer, Damaru, Oni Hunter''s Garb, Hydra''s Lament,
    Breastplate of Valor, Shogun''s Ofuda, Eye of the Storm, Shield Splitter, Shield
    of the Phoenix, Spectral Armor, Freya''s Tears, Dominance, Avenging Blade, Tyrfing,
    Erosion, Riptalon, Yogi''s Necklace, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.49
      pick: 0.16
      fit: 0.57
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.5
      win: 0.63
      pick: 0.17
      fit: 0.25
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.37
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Riptalon, Pharaoh''s
    Curse, The Crusher, Jotunn''s Revenge, Oni Hunter''s Garb, Runeforged Hammer,
    The Reaper, Chandra''s Grace, Lernaean Bow, Breastplate of Valor, Shogun''s Ofuda,
    Damaru, Phoenix Feather, Freya''s Tears, Hydra''s Lament, Eye of the Storm, Shield
    Splitter, Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s
    Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.47
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.54
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.63
    Hide of the Nemean Lion:
      total: 0.51
      efficiency: 0.5
      win: 0.63
      pick: 0.17
      fit: 0.3
    Shifter's Shield:
      total: 0.5
      efficiency: 0.52
      win: 0.49
      pick: 0.58
      fit: 0.44
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.49
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
  - Hide of the Nemean Lion
  - The Crusher
  flex_slots:
  - Hide of the Nemean Lion
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
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Genji''s Guard,
    Riptalon, Amanita Charm, Silverbranch Bow, Stone of Binding, Pharaoh''s Curse,
    Void Shield, Lernaean Bow, Runeforged Hammer, The Reaper, Oni Hunter''s Garb,
    Screeching Gargoyle, Tekko-Kagi, Breastplate of Valor, Hydra''s Lament, Damaru,
    Void Stone, Heartseeker, Shogun''s Ofuda, Spectral Armor, Freya''s Tears, Shield
    of the Phoenix, Toxic Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.48
      win: 0.49
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.17
      fit: 0.19
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.49
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
  - Hide of the Nemean Lion
  - Riptalon
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Genji''s Guard, Pharaoh''s Curse, Amanita Charm, The Crusher,
    Jotunn''s Revenge, Lernaean Bow, Silverbranch Bow, Oni Hunter''s Garb, Tyrfing,
    Breastplate of Valor, Shogun''s Ofuda, Runeforged Hammer, Hydra''s Lament, Damaru,
    Spectral Armor, Freya''s Tears, Shield of the Phoenix, Eros'' Bow, Dominance,
    Yogi''s Necklace, Toxic Blade, Eye of the Storm, Erosion, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.49
      pick: 0.16
      fit: 0.6
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.41
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.17
      fit: 0.19
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Breastplate of Valor, Hydra''s Lament, Freya''s Tears, Shield of the Phoenix,
    Amanita Charm, The Crusher, Pharaoh''s Curse, Oni Hunter''s Garb, Chandra''s Grace,
    Screeching Gargoyle, Lernaean Bow, Runeforged Hammer, Damaru, Spectral Armor,
    Shogun''s Ofuda, Gladiator''s Shield, Yogi''s Necklace, Riptalon, Arondight, Erosion,
    Leviathan''s Hide, Eye of the Storm, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.33
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.5
      efficiency: 0.5
      win: 0.63
      pick: 0.17
      fit: 0.18
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
    Underrated for this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Genji''s
    Guard, Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer, Damaru, Oni Hunter''s
    Garb, Hydra''s Lament, Breastplate of Valor, Shogun''s Ofuda, Eye of the Storm,
    Shield Splitter, Shield of the Phoenix, Spectral Armor, Freya''s Tears, Dominance,
    Avenging Blade, Tyrfing, Erosion, Riptalon, Yogi''s Necklace, Eye of Providence,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.49
      pick: 0.16
      fit: 0.57
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.44
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.49
      pick: 0.3
      fit: 0.45
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.49
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.35
  starter: *id001
---
