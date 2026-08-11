---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.59
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.25
      win_rate: 0.51
    - name: Devourer's Gauntlet
      pick_rate: 0.07
      win_rate: 0.5
  - name: Prophetic Cloak
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.39
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.68
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.37
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.1
      win_rate: 0.63
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.65
  - name: Ethereal Staff
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.48
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.72
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.54
  - name: Soul Reaver
    pick_rate: 0.07
    win_rate: 0.73
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.38
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.39
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.43
  - name: Death's Embrace
    pick_rate: 0.09
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-10'
  god_win_rate: 0.5289855072463768
  god_matches_won: 219
  god_matches_played: 414
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Soul Reaver
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, Breastplate of Valor, The
    Crusher, Oni Hunter''s Garb, Golden Blade, Shield Splitter, Hydra''s Lament, Shield
    of the Phoenix, Lernaean Bow, Runeforged Hammer, Shogun''s Ofuda, Erosion, Eye
    of Providence, Eye of the Storm, Spectral Armor, Soul Gem, Draconic Scale, Death
    Metal, Leviathan''s Hide, Mantle Of Discord, Helm of Radiance, Midgardian Mail,
    Stone of Binding, Damaru, Avenging Blade, Dominance, Bracer of The Abyss, Bragi''s
    Harp, Tyrfing, Yogi''s Necklace, Riptalon, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.48
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.15
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.48
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
  - Soul Reaver
  - Amanita Charm
  flex_slots:
  - Soul Reaver
  - Kinetic Cuirass
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Soul Gem,
    Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Pharaoh''s
    Curse, Riptalon, The Crusher, Golden Blade, Chandra''s Grace, Oni Hunter''s Garb,
    Breastplate of Valor, Runeforged Hammer, Freya''s Tears, The Reaper, Hydra''s
    Lament, Lernaean Bow, Shogun''s Ofuda, Blood-Bound Book, Bancroft''s Talon, Phoenix
    Feather, Eye of the Storm, Shield Splitter, Spectral Armor, Erosion, Eye of Providence,
    Draconic Scale, Lifebinder, Death Metal, Leviathan''s Hide, Avenging Blade, Midgardian
    Mail, Yogi''s Necklace, Damaru, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.46
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.15
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Reaver
  flex_slots:
  - Berserker's Shield
  - Soul Reaver
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
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Breastplate of Valor, Void Shield, Freya''s Tears, Spear
    of the Magus, Pharaoh''s Curse, Riptalon, Oni Hunter''s Garb, Hydra''s Lament,
    The Cosmic Horror, Silverbranch Bow, Void Stone, Golden Blade, Runeforged Hammer,
    Lernaean Bow, Shield of the Phoenix, The Reaper, Shield Splitter, Spectral Armor,
    Shogun''s Ofuda, Spear of Desolation, Tekko-Kagi, Erosion, Obsidian Shard, Eye
    of Providence, Eye of the Storm, Heartseeker, Death Metal, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.37
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.5
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Gluttonous Grimoire
  - Shifter's Shield
  - Soul Reaver
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Breastplate of Valor, Riptalon,
    The Crusher, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s
    Ofuda, Hydra''s Lament, Shield of the Phoenix, Silverbranch Bow, Tyrfing, Runeforged
    Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of
    The Abyss, Draconic Scale, Eye of the Storm, Helm of Radiance, Leviathan''s Hide,
    Death Metal, Midgardian Mail, Mantle Of Discord, Stone of Binding, Yogi''s Necklace,
    Dominance, Eros'' Bow, Damaru, Spear of the Magus.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.37
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.13
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Soul Reaver
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Breastplate of
    Valor, Jotunn''s Revenge, Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Pharaoh''s Curse,
    Oni Hunter''s Garb, The Crusher, Chronos'' Pendant, Screeching Gargoyle, Spear
    of Desolation, Shogun''s Ofuda, Chandra''s Grace, Spectral Armor, Erosion, Golden
    Blade, Lernaean Bow, Runeforged Hammer, Gladiator''s Shield, Eye of Providence,
    Helm of Radiance, Shield Splitter, Draconic Scale, Gem of Focus, Death Metal,
    Bracer of The Abyss, Leviathan''s Hide, Spear of the Magus, Rod of Asclepius,
    Eye of the Storm, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.39
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.18
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Reaver
  flex_slots:
  - Soul Reaver
  - The Crusher
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Amanita Charm, Breastplate of Valor, Hydra''s
    Lament, Freya''s Tears, Soul Gem, Runeforged Hammer, Shield Splitter, Oni Hunter''s
    Garb, Golden Blade, Pharaoh''s Curse, Lernaean Bow, Eye of the Storm, Shield of
    the Phoenix, Death Metal, Erosion, Spectral Armor, Eye of Providence, Spear of
    the Magus, Damaru, The Reaper, Shogun''s Ofuda, Draconic Scale, Avenging Blade,
    The Cosmic Horror, Leviathan''s Hide, Riptalon, Helm of Radiance, Midgardian Mail,
    Mantle Of Discord, Heartseeker, Stone of Binding, Tekko-Kagi, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
    Soul Reaver:
      total: 0.52
      efficiency: 0.45
      win: 0.73
      pick: 0.22
      fit: 0.14
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Reaver
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem,
    Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Oni Hunter''s Garb, Spear
    of the Magus, Death Metal, Hydra''s Lament, Runeforged Hammer, Lernaean Bow, Golden
    Blade, The Cosmic Horror, Helm of Radiance, Shield of the Phoenix, Shield Splitter,
    Bracer of The Abyss, Spectral Armor, Shogun''s Ofuda, Rod of Asclepius, Spear
    of Desolation, Erosion, Bragi''s Harp, Eye of the Storm, Riptalon, Jade Scepter,
    Eye of Providence, Obsidian Shard, Chronos'' Pendant, Draconic Scale, Damaru,
    Silverbranch Bow, Blood-Bound Book.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.59
      pick: 0.34
      fit: 0.36
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Reaver:
      total: 0.53
      efficiency: 0.45
      win: 0.73
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
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Gluttonous Grimoire, Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, Breastplate
    of Valor, The Crusher, Oni Hunter''s Garb, Golden Blade, Shield Splitter, Hydra''s
    Lament, Shield of the Phoenix, Lernaean Bow, Runeforged Hammer, Shogun''s Ofuda,
    Erosion, Eye of Providence, Eye of the Storm, Spectral Armor, Soul Gem, Draconic
    Scale, Death Metal, Leviathan''s Hide, Mantle Of Discord, Helm of Radiance, Midgardian
    Mail, Stone of Binding, Damaru, Avenging Blade, Dominance, Bracer of The Abyss,
    Bragi''s Harp, Tyrfing, Yogi''s Necklace, Riptalon, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.71
      win: 0.37
      pick: 0.23
      fit: 0.26
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
