---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.58
    alternates:
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.48
    - name: Shield of the Phoenix
      pick_rate: 0.04
      win_rate: 0.55
  - name: Shield of the Phoenix
    pick_rate: 0.23
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.51
  - name: Gladiator's Shield
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.55
    - name: Shield of the Phoenix
      pick_rate: 0.13
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.58
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.61
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.74
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.73
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.68
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.49
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.39
    win_rate: 0.48
  - name: Bumba's Golden Dagger
    pick_rate: 0.09
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-21'
  god_win_rate: 0.5568942436412316
  god_matches_won: 416
  god_matches_played: 747
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Amanita Charm, The Crusher, Jotunn''s
    Revenge, Gluttonous Grimoire, Berserker''s Shield, Breastplate of Valor, Oni Hunter''s
    Garb, Shield Splitter, Erosion, Runeforged Hammer, Soul Gem, Eye of Providence,
    Eye of the Storm, Hydra''s Lament, Spectral Armor, Draconic Scale, Nimble Ring,
    Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Golden
    Blade, Stone of Binding, Avenging Blade, The Reaper, The Cosmic Horror, Death
    Metal, Magi''s Cloak, Spear of the Magus, Helm of Radiance, Screeching Gargoyle,
    Ancile, Damaru, Spear of Desolation, Shogun''s Ofuda, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.61
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.47
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.51
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Amanita Charm, Soul Gem, Nimble Ring, Breastplate of Valor, Berserker''s Shield,
    Hydra''s Lament, Oni Hunter''s Garb, Death Metal, Runeforged Hammer, The Cosmic
    Horror, Shield Splitter, Spear of the Magus, Obsidian Shard, Spear of Desolation,
    Helm of Radiance, Eye of the Storm, Spectral Armor, Ethereal Staff, Erosion, Rod
    of Asclepius, Eye of Providence, Chronos'' Pendant, Heartseeker, Draconic Scale,
    Golden Blade, Jade Scepter, The Reaper, Pharaoh''s Curse, Damaru, Leviathan''s
    Hide, Avenging Blade, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.46
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, The
    Crusher, Soul Gem, Amanita Charm, Berserker''s Shield, Breastplate of Valor, Nimble
    Ring, The Cosmic Horror, Spear of Desolation, Spear of the Magus, Oni Hunter''s
    Garb, Hydra''s Lament, Obsidian Shard, Runeforged Hammer, Shield Splitter, Spectral
    Armor, Erosion, Death Metal, Eye of Providence, Helm of Radiance, Eye of the Storm,
    The Reaper, Chronos'' Pendant, Draconic Scale, Ethereal Staff, Pharaoh''s Curse,
    Rod of Asclepius, Screeching Gargoyle, Leviathan''s Hide, Heartseeker, Midgardian
    Mail, Mantle Of Discord, Golden Blade, Titan''s Bane, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - The Crusher
  - Amanita Charm
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Soul Gem, Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Berserker''s Shield, The Reaper, Ethereal Staff,
    Chandra''s Grace, Yogi''s Necklace, Rod of Asclepius, Runeforged Hammer, Oni Hunter''s
    Garb, Breastplate of Valor, Eye of the Storm, Phoenix Feather, Erosion, Hydra''s
    Lament, Shield Splitter, Riptalon, Spectral Armor, Eye of Providence, Draconic
    Scale, Nimble Ring, Golden Blade, Blood-Bound Book, Pharaoh''s Curse, Leviathan''s
    Hide, Avenging Blade, Lifebinder, Midgardian Mail, Bancroft''s Talon, Death Metal,
    The Cosmic Horror, Glorious Pridwen, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.31
      fit: 0.74
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.41
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, The Crusher, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Stone of Binding, Berserker''s Shield,
    Avenging Blade, Screeching Gargoyle, Void Shield, Breastplate of Valor, Oni Hunter''s
    Garb, The Cosmic Horror, Void Stone, The Reaper, Spear of the Magus, Runeforged
    Hammer, Shield Splitter, Obsidian Shard, Hydra''s Lament, Spear of Desolation,
    Nimble Ring, Erosion, Heartseeker, Spectral Armor, Eye of Providence, Eye of the
    Storm, Titan''s Bane, Draconic Scale, Pharaoh''s Curse, Riptalon, Leviathan''s
    Hide, Midgardian Mail, Silverbranch Bow, Golden Blade, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Gluttonous Grimoire
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Rod of Tahuti, Nimble Ring, Gluttonous
    Grimoire, Amanita Charm, The Crusher, Jotunn''s Revenge, Golden Blade, Riptalon,
    Pharaoh''s Curse, Soul Gem, Breastplate of Valor, Oni Hunter''s Garb, Silverbranch
    Bow, Shogun''s Ofuda, Runeforged Hammer, Tyrfing, Spectral Armor, Hydra''s Lament,
    Lernaean Bow, Erosion, Shield Splitter, Eye of Providence, Toxic Blade, Draconic
    Scale, Eye of the Storm, Leviathan''s Hide, The Cosmic Horror, Dominance, Midgardian
    Mail, The Reaper, Spear of the Magus, Mantle Of Discord, Helm of Radiance, Stone
    of Binding, Obsidian Shard, Death Metal.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.44
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.28
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.31
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Breastplate of Valor, Soul Gem, Gluttonous Grimoire, Amanita Charm, The
    Crusher, Berserker''s Shield, Hydra''s Lament, Spear of Desolation, Oni Hunter''s
    Garb, Screeching Gargoyle, Nimble Ring, Chronos'' Pendant, Chandra''s Grace, Erosion,
    Spectral Armor, Eye of Providence, Runeforged Hammer, Totem of Death, Prophetic
    Cloak, Shield Splitter, Draconic Scale, The Cosmic Horror, Pharaoh''s Curse, Spear
    of the Magus, Leviathan''s Hide, Helm of Radiance, Eye of the Storm, Gem of Focus,
    Midgardian Mail, Obsidian Shard, Mantle Of Discord, Stone of Binding, Ethereal
    Staff, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.44
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.51
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.31
      fit: 0.56
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher, Amanita Charm, Nimble Ring,
    Berserker''s Shield, Breastplate of Valor, The Cosmic Horror, Spear of the Magus,
    Oni Hunter''s Garb, Spear of Desolation, Death Metal, Hydra''s Lament, Obsidian
    Shard, Helm of Radiance, Runeforged Hammer, Shield Splitter, Ethereal Staff, Spectral
    Armor, Erosion, Rod of Asclepius, Chronos'' Pendant, Eye of Providence, Eye of
    the Storm, Jade Scepter, Draconic Scale, Pharaoh''s Curse, Totem of Death, Leviathan''s
    Hide, Midgardian Mail, The Reaper, Screeching Gargoyle, Golden Blade, Mantle Of
    Discord, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Gluttonous
    Grimoire, The Crusher, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Breastplate of Valor, Oni Hunter''s Garb, The Cosmic Horror,
    Runeforged Hammer, Shield Splitter, Death Metal, Spear of the Magus, Hydra''s
    Lament, Obsidian Shard, Erosion, Spear of Desolation, Eye of the Storm, Helm of
    Radiance, Spectral Armor, Eye of Providence, Ethereal Staff, Draconic Scale, Rod
    of Asclepius, Pharaoh''s Curse, The Reaper, Leviathan''s Hide, Golden Blade, Chronos''
    Pendant, Jade Scepter, Midgardian Mail, Avenging Blade, Mantle Of Discord, Damaru,
    Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.73
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, The Crusher, Jotunn''s
    Revenge, Gluttonous Grimoire, Berserker''s Shield, Freya''s Tears, Breastplate
    of Valor, Oni Hunter''s Garb, Shield Splitter, Erosion, Runeforged Hammer, Soul
    Gem, Eye of Providence, Eye of the Storm, Hydra''s Lament, Spectral Armor, Draconic
    Scale, Nimble Ring, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Golden Blade, Stone of Binding, Avenging Blade, The Reaper, The Cosmic
    Horror, Death Metal, Magi''s Cloak, Spear of the Magus, Helm of Radiance, Screeching
    Gargoyle, Ancile, Damaru, Spear of Desolation, Shogun''s Ofuda, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.27
      fit: 0.28
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.15
      fit: 0.61
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.51
  starter: *id001
---
