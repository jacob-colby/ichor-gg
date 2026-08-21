---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.39
  aspect_win_rate: 0.42
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.26
    win_rate: 0.36
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.75
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.67
  - name: Shield of the Phoenix
    pick_rate: 0.07
    win_rate: 0.29
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.41
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.31
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.38
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.5
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.2
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.14
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.0
  - name: Heartseeker
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.2
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.2
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.25
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.0
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.4
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.22
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-21'
  god_win_rate: 0.42857142857142855
  god_matches_won: 42
  god_matches_played: 98
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Crusher
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Rod of Tahuti, Ethereal Staff, Gluttonous Grimoire,
    Kinetic Cuirass, Amanita Charm, The Crusher, Breastplate of Valor, Berserker''s
    Shield, Soul Gem, Nimble Ring, Oni Hunter''s Garb, Shield Splitter, Runeforged
    Hammer, The Cosmic Horror, Erosion, Hydra''s Lament, Spectral Armor, Eye of Providence,
    Spear of the Magus, Eye of the Storm, Death Metal, Obsidian Shard, Draconic Scale,
    Helm of Radiance, Spear of Desolation, Pharaoh''s Curse, Shield of the Phoenix,
    Leviathan''s Hide, Rod of Asclepius, Midgardian Mail, Golden Blade, The Reaper,
    Mantle Of Discord, Stone of Binding, Jade Scepter, Avenging Blade, Chronos'' Pendant,
    Damaru, Freya''s Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.64
      win: 0.38
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.34
      pick: 0.0
      fit: 0.55
    Ethereal Staff:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.38
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.52
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - The Crusher
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Rod of Tahuti, Ethereal Staff, Gluttonous Grimoire, Breastplate of Valor,
    The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem, Nimble Ring, Berserker''s
    Shield, Hydra''s Lament, Oni Hunter''s Garb, Death Metal, Runeforged Hammer, The
    Cosmic Horror, Shield Splitter, Spear of the Magus, Obsidian Shard, Spear of Desolation,
    Helm of Radiance, Eye of the Storm, Spectral Armor, Erosion, Rod of Asclepius,
    Eye of Providence, Chronos'' Pendant, Draconic Scale, Golden Blade, Jade Scepter,
    The Reaper, Pharaoh''s Curse, Shield of the Phoenix, Damaru, Leviathan''s Hide,
    Avenging Blade, Yogi''s Necklace, Midgardian Mail, Freya''s Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.64
      win: 0.38
      pick: 0.14
      fit: 0.29
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.45
    Ethereal Staff:
      total: 0.47
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.39
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.4
    Heartseeker:
      total: 0.54
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.56
    Rod of Tahuti:
      total: 0.48
      efficiency: 0.77
      win: 0.34
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Ethereal Staff
  - The Crusher
  - Heartseeker
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Rod of Tahuti, Ethereal Staff, Gluttonous Grimoire, The
    Crusher, Breastplate of Valor, Soul Gem, Kinetic Cuirass, Amanita Charm, Berserker''s
    Shield, Nimble Ring, The Cosmic Horror, Spear of Desolation, Spear of the Magus,
    Oni Hunter''s Garb, Hydra''s Lament, Obsidian Shard, Runeforged Hammer, Shield
    Splitter, Spectral Armor, Erosion, Death Metal, Eye of Providence, Shield of the
    Phoenix, Helm of Radiance, Eye of the Storm, The Reaper, Chronos'' Pendant, Draconic
    Scale, Pharaoh''s Curse, Rod of Asclepius, Screeching Gargoyle, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Golden Blade, Titan''s Bane, Chandra''s Grace,
    Freya''s Tears.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.69
      win: 0.31
      pick: 0.26
      fit: 0.27
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.64
      win: 0.38
      pick: 0.14
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.48
    Ethereal Staff:
      total: 0.46
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.35
    The Crusher:
      total: 0.45
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Jotunn''s Revenge, Ethereal Staff, Amanita Charm, Soul Gem, Rod of Tahuti,
    Gluttonous Grimoire, The Crusher, Kinetic Cuirass, Rod of Asclepius, Shield of
    the Phoenix, Breastplate of Valor, The Reaper, Berserker''s Shield, Yogi''s Necklace,
    Chandra''s Grace, Nimble Ring, Blood-Bound Book, Oni Hunter''s Garb, Runeforged
    Hammer, Riptalon, Bancroft''s Talon, Lifebinder, The Cosmic Horror, Phoenix Feather,
    Hydra''s Lament, Spectral Armor, Eye of the Storm, Spear of the Magus, Death Metal,
    Erosion, Shield Splitter, Obsidian Shard, Spear of Desolation, Eye of Providence,
    Draconic Scale, Helm of Radiance, Golden Blade, Pharaoh''s Curse, Leviathan''s
    Hide, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.42
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.34
      pick: 0.0
      fit: 0.53
    Ethereal Staff:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.72
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.43
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.53
    Amanita Charm:
      total: 0.48
      efficiency: 0.63
      win: 0.34
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Heartseeker
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Rod of Tahuti, Gluttonous Grimoire, Ethereal
    Staff, The Crusher, Soul Gem, Kinetic Cuirass, Amanita Charm, Breastplate of Valor,
    Stone of Binding, Berserker''s Shield, Avenging Blade, The Cosmic Horror, Screeching
    Gargoyle, Spear of the Magus, Nimble Ring, Void Shield, Obsidian Shard, Spear
    of Desolation, Oni Hunter''s Garb, Void Stone, Runeforged Hammer, The Reaper,
    Hydra''s Lament, Shield Splitter, Spectral Armor, Erosion, Death Metal, Eye of
    Providence, Eye of the Storm, Helm of Radiance, Titan''s Bane, Draconic Scale,
    Pharaoh''s Curse, Riptalon, Rod of Asclepius, Leviathan''s Hide, Shield of the
    Phoenix, Freya''s Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.64
      win: 0.38
      pick: 0.14
      fit: 0.21
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.49
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.59
      win: 0.34
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.63
      win: 0.34
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.46
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.52
    Heartseeker:
      total: 0.55
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Ethereal Staff
  - Heartseeker
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Rod of Tahuti, Ethereal Staff, Gluttonous Grimoire,
    Nimble Ring, Berserker''s Shield, Breastplate of Valor, Kinetic Cuirass, The Crusher,
    Amanita Charm, Soul Gem, Golden Blade, Riptalon, Pharaoh''s Curse, Oni Hunter''s
    Garb, Silverbranch Bow, The Cosmic Horror, Runeforged Hammer, Spectral Armor,
    Hydra''s Lament, Shogun''s Ofuda, Spear of the Magus, Tyrfing, Lernaean Bow, Erosion,
    Obsidian Shard, Helm of Radiance, Shield Splitter, Death Metal, Eye of Providence,
    Spear of Desolation, Toxic Blade, Draconic Scale, Rod of Asclepius, Leviathan''s
    Hide, Eye of the Storm, The Reaper, Bracer of The Abyss, Shield of the Phoenix,
    Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.41
      efficiency: 0.53
      win: 0.34
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.44
      efficiency: 0.66
      win: 0.34
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.25
    Nimble Ring:
      total: 0.44
      efficiency: 0.68
      win: 0.34
      pick: 0.0
      fit: 0.33
    Ethereal Staff:
      total: 0.45
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.29
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - Heartseeker
  flex_slots:
  - Ethereal Staff
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Rod of Tahuti, Ethereal Staff, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Prophetic Cloak, The Crusher, Berserker''s Shield, Hydra''s Lament,
    Shield of the Phoenix, Spear of Desolation, Oni Hunter''s Garb, Nimble Ring, Screeching
    Gargoyle, Chronos'' Pendant, Chandra''s Grace, Erosion, Gladiator''s Shield, Spectral
    Armor, Eye of Providence, Runeforged Hammer, Totem of Death, The Cosmic Horror,
    Shield Splitter, Draconic Scale, Spear of the Magus, Freya''s Tears, Pharaoh''s
    Curse, Obsidian Shard, Leviathan''s Hide, Helm of Radiance, Eye of the Storm,
    Midgardian Mail, Gem of Focus, Mantle Of Discord, Stone of Binding, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.69
      win: 0.31
      pick: 0.26
      fit: 0.43
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.64
      win: 0.38
      pick: 0.14
      fit: 0.43
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.51
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.34
      pick: 0.0
      fit: 0.5
    Ethereal Staff:
      total: 0.45
      efficiency: 0.51
      win: 0.5
      pick: 0.09
      fit: 0.3
    Heartseeker:
      total: 0.52
      efficiency: 0.41
      win: 0.67
      pick: 0.15
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, The Crusher, Jotunn''s Revenge, Berserker''s Shield, Soul Gem,
    Freya''s Tears, Nimble Ring, Breastplate of Valor, Oni Hunter''s Garb, Shield
    of the Phoenix, Shield Splitter, Runeforged Hammer, The Cosmic Horror, Erosion,
    Hydra''s Lament, Spectral Armor, Eye of Providence, Spear of the Magus, Eye of
    the Storm, Death Metal, Obsidian Shard, Draconic Scale, Helm of Radiance, Spear
    of Desolation, Ethereal Staff, Pharaoh''s Curse, Leviathan''s Hide, Rod of Asclepius,
    Midgardian Mail, Golden Blade, The Reaper, Mantle Of Discord, Stone of Binding,
    Jade Scepter, Avenging Blade, Chronos'' Pendant, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.69
      win: 0.31
      pick: 0.26
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.67
      pick: 0.06
      fit: 0.4
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.59
      win: 0.34
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.63
      win: 0.34
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.44
      efficiency: 0.64
      win: 0.34
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.77
      win: 0.34
      pick: 0.0
      fit: 0.3
  starter: *id001
---
