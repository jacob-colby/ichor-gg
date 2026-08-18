---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.67
    alternates:
    - name: Golden Blade
      pick_rate: 0.21
      win_rate: 0.53
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.4
  - name: Golden Blade
    pick_rate: 0.33
    win_rate: 0.64
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.2
      win_rate: 0.68
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.33
  - name: Kinetic Cuirass
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.58
    - name: Shogun's Ofuda
      pick_rate: 0.11
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.12
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.69
  - name: Berserker's Shield
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.75
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.5
  - name: Medallion
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.83
    - name: Shogun's Ofuda
      pick_rate: 0.07
      win_rate: 0.8
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.37
    win_rate: 0.7
  - name: Death's Toll
    pick_rate: 0.3
    win_rate: 0.48
  - name: Bumba's Golden Dagger
    pick_rate: 0.07
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-08-18'
  god_win_rate: 0.6197183098591549
  god_matches_won: 88
  god_matches_played: 142
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-18'
  god_matches_analyzed: 8839
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, The Crusher, Gluttonous Grimoire, Breastplate of Valor, Shield Splitter,
    Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Eye of Providence, Runeforged
    Hammer, Eye of the Storm, Hydra''s Lament, Draconic Scale, Spectral Armor, Soul
    Gem, Nimble Ring, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Avenging Blade, Death Metal, Screeching Gargoyle,
    Magi''s Cloak, Ancile, Helm of Radiance, Gladiator''s Shield, Damaru, Void Shield,
    Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.36
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.4
      fit: 0.67
    Shifter's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.45
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.57
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.36
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Genji''s Guard, Rod
    of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Chandra''s Grace, The Crusher,
    Rod of Asclepius, Freya''s Tears, Runeforged Hammer, Oni Hunter''s Garb, The Reaper,
    Breastplate of Valor, Eye of the Storm, Erosion, Phoenix Feather, Shield Splitter,
    Hydra''s Lament, Eye of Providence, Spectral Armor, Draconic Scale, Pharaoh''s
    Curse, Nimble Ring, Leviathan''s Hide, Avenging Blade, Blood-Bound Book, Midgardian
    Mail, Lifebinder, Glorious Pridwen, Bancroft''s Talon, Riptalon, Death Metal,
    Ancile, Gladiator''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.4
      fit: 0.65
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.59
      efficiency: 0.52
      win: 0.67
      pick: 0.45
      fit: 0.55
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.85
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    Amanita Charm, Soul Gem, Genji''s Guard, Stone of Binding, Avenging Blade, Screeching
    Gargoyle, Freya''s Tears, Void Shield, Breastplate of Valor, Oni Hunter''s Garb,
    The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear of the Magus, The
    Reaper, Runeforged Hammer, Spear of Desolation, Hydra''s Lament, Shield Splitter,
    Nimble Ring, Erosion, Spectral Armor, Eye of Providence, Eye of the Storm, Draconic
    Scale, Obsidian Shard, Pharaoh''s Curse, Riptalon, Leviathan''s Hide, Midgardian
    Mail, Heartseeker, Silverbranch Bow, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.27
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.45
      fit: 0.42
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.55
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Rod of Tahuti, Amanita Charm, Genji''s Guard, Gluttonous
    Grimoire, The Crusher, Pharaoh''s Curse, Freya''s Tears, Jotunn''s Revenge, Breastplate
    of Valor, Riptalon, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Tyrfing,
    Runeforged Hammer, Spectral Armor, Hydra''s Lament, Erosion, Lernaean Bow, Silverbranch
    Bow, Shield Splitter, Eye of Providence, Draconic Scale, Eye of the Storm, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Toxic Blade, Stone of Binding, Helm
    of Radiance, Screeching Gargoyle, Death Metal, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.53
      win: 0.64
      pick: 0.45
      fit: 0.53
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.43
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.67
      pick: 0.45
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.36
    Shogun's Ofuda:
      total: 0.61
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Shield of the Phoenix
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Jotunn''s Revenge, Shield of the Phoenix, Rod of Tahuti, Amanita Charm,
    Soul Gem, Gluttonous Grimoire, Hydra''s Lament, The Crusher, Screeching Gargoyle,
    Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s Grace, Spear of
    Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic
    Cloak, Shield Splitter, Draconic Scale, Runeforged Hammer, Pharaoh''s Curse, Eye
    of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian Mail,
    Mantle Of Discord, Totem of Death, Stone of Binding, Arondight, Death Metal, Rod
    of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.64
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire, Soul
    Gem, Jotunn''s Revenge, The Crusher, Genji''s Guard, Amanita Charm, Nimble Ring,
    Freya''s Tears, Breastplate of Valor, The Cosmic Horror, Shield of the Phoenix,
    Spear of the Magus, Spear of Desolation, Oni Hunter''s Garb, Death Metal, Hydra''s
    Lament, Helm of Radiance, Runeforged Hammer, Shield Splitter, Spectral Armor,
    Erosion, Rod of Asclepius, Chronos'' Pendant, Eye of Providence, Eye of the Storm,
    Obsidian Shard, Jade Scepter, Draconic Scale, Pharaoh''s Curse, Leviathan''s Hide,
    Ethereal Staff, Midgardian Mail, The Reaper, Screeching Gargoyle, Mantle Of Discord,
    Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.25
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.25
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.38
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Soul Gem, Nimble
    Ring, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb, The Cosmic Horror,
    Runeforged Hammer, Shield of the Phoenix, Hydra''s Lament, Shield Splitter, Death
    Metal, Spear of the Magus, Spear of Desolation, Erosion, Helm of Radiance, Eye
    of the Storm, Spectral Armor, Eye of Providence, Draconic Scale, Rod of Asclepius,
    Pharaoh''s Curse, Chronos'' Pendant, The Reaper, Obsidian Shard, Leviathan''s
    Hide, Jade Scepter, Midgardian Mail, Avenging Blade, Mantle Of Discord, Damaru,
    Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.45
      fit: 0.41
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.42
    Shogun's Ofuda:
      total: 0.59
      efficiency: 0.51
      win: 0.8
      pick: 0.22
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Rod of Tahuti, Freya''s
    Tears, Jotunn''s Revenge, The Crusher, Gluttonous Grimoire, Breastplate of Valor,
    Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Eye of Providence,
    Runeforged Hammer, Eye of the Storm, Hydra''s Lament, Draconic Scale, Spectral
    Armor, Soul Gem, Nimble Ring, Pharaoh''s Curse, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Avenging Blade, Death Metal, Screeching
    Gargoyle, Magi''s Cloak, Ancile, Helm of Radiance, Gladiator''s Shield, Damaru,
    Void Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.32
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.26
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.64
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.4
      fit: 0.67
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.57
  starter: *id001
---
